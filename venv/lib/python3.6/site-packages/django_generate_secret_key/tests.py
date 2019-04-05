from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO
import shutil
import os
from generate_secret_key.management.commands.generate_secret_key import Command


class ImportCsvCommandTests(TestCase):
    command_name = 'generate_secret_key'

    BASE_DIR = '/tmp/django_generate_secret_key_tests/'

    def setUp(self):
        self.out = StringIO()
        self.err = StringIO()
        # Monkey patch to test dissociate from the real directory / secret key
        Command.BASE_DIR = self.BASE_DIR
        # Try to remove the directory
        try:
            shutil.rmtree(self.BASE_DIR)
        except FileNotFoundError:
            pass
        # Create it
        os.mkdir(self.BASE_DIR)

    def tearDown(self):
        shutil.rmtree(self.BASE_DIR)

    def test_create_simple(self):
        call_command(self.command_name, stdout=self.out, stderr=self.err)

        self._check_valid_key()

    def test_error_on_too_much_params(self):
        call_command(
            self.command_name,
            "f1", "f2", "f3",
            stdout=self.out,
            stderr=self.err
        )

        self.assertEqual(
            self.err.getvalue(),
            "Please provide only one file name (or none).\n",
        )

    def test_existing_key(self):
        call_command(self.command_name, stdout=self.out, stderr=self.err)

        self.assertEqual(self.err.getvalue(), "",)

        call_command(self.command_name, stdout=self.out, stderr=self.err)

        self.assertEqual(
            self.err.getvalue(),
            "There is already a secret key in `secretkey.txt`\n",
        )

    def test_replacing_key(self):
        call_command(self.command_name, stdout=self.out, stderr=self.err)
        previous_key = self._read_key()

        call_command(self.command_name, replace=True, stdout=self.out, stderr=self.err)
        new_key = self._read_key()

        self.assertNotEqual(
            previous_key,
            new_key,
        )

        self.assertEqual(self.err.getvalue(), "",)

    def test_alternative_name(self):
        filename = "altsecretkey.txt"

        call_command(
            self.command_name,
            filename,
            stdout=self.out, stderr=self.err
        )

        self._check_valid_key(filename)
        self.assertTrue(os.path.isfile(self.BASE_DIR + filename))
        self.assertFalse(os.path.isfile(self.BASE_DIR + "secretkey.txt"))

    def _check_valid_key(self, filename='secretkey.txt'):
        """ Checks if the key is created and valid """
        key = self._read_key(filename)
        self.assertEqual(len(key), 50)

    def _read_key(self, filename='secretkey.txt'):
        """ Reads and return the given key """
        try:
            keyfile = open(self.BASE_DIR + filename)
        except FileNotFoundError:
            self.fail("The file `{}` wasn't created".format(filename))

        return keyfile.read()
