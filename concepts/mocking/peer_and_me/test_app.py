import unittest
from unittest.mock import Mock
import mock
import app

### Mocking approach !! ###
### THE MOKING LIBARY
#print(dir(mock))
class Test(unittest.TestCase):
    @mock.patch("app.os.path")
    @mock.patch("app.os")
    @mock.patch("app.rm")
    def test_remove2(self, mock_app_rm_remove, mock_app_os, mock_app_os_path):
        # set up the mock
        mock_app_rm_remove.return_value = [1, 3, 3]
        x = app.rm("some file")
        print(mock_app_rm_remove)
        print("rm return: ", x)

        # TEST 1 - NO REMOVE -> FILE.EXIST = FALSE
        mock_app_os_path.isfile.return_value = False
        print("FALSE", app.rm("any path"))
        # test that the remove call was NOT called.
        self.assertFalse(
            mock_app_os.remove.called, "Failed to not remove the file if not present."
        )

        # TEST 2 - REMOVE -> FILE.EXIST = TRUE
        mock_app_os_path.isfile.return_value = True
        print("TRUE", app.rm("any path"))
        self.assertFalse(
            mock_app_os.remove.called, "Failed to not remove the file if not present."
        )


if __name__ == "__main__":
    unittest.main()