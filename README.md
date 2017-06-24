# SysAdmin & DevOps

![SysAdmin and DevOps](https://raw.githubusercontent.com/srinitude/holbertonschool-sysadmin_devops/master/SysAdminDevOpsTopicImage.jpg)

Credits: [Sellorekt](https://soundcloud.com/sellorekt/the-harder-it-gets)

## Table of Contents
1. [Shell Basics](https://github.com/srinitude/holbertonschool-sysadmin_devops/tree/master/0x00-shell_basics)
   * [Write a script that prints the absolute path name of the current working directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/0-current_working_directory)
   * [Display the contents list of your current directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/1-listit)
   * [Write a script that changes the working directory to the user’s home directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/2-bring_me_home)
   * [Display current directory contents in a long format.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/3-listfiles)
   * [Display current directory contents, including hidden files (starting with .), with the long format.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/4-listmorefiles)
   * [Display current directory contents with the long format, user/group IDs displyed numerically, and hidden files.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)
   * [Create a script that creates a directory named `holberton` in the `/tmp/` directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/6-firstdirectory)
   * [Move the file `betty` from `/tmp/` to `/tmp/holberton`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/7-movethatfile)
   * [Delete the file `betty` - the file `betty` is in `/tmp/holberton`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/8-firstdelete)
   * [Delete the directory `holberton` that is in the `/tmp/` directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/9-firstdirdeletion)
   * [Write a script that changes the working directory to the previous one.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/10-back)
   * [Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot/` directory (in this order), in long format.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/11-lists)
   * [Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp/` directory when we will run your script.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/12-file_type)
   * [Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/13-symbolic_link)
   * [Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/14-copy_html)
   * [Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u/`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/15-lets_move)
   * [Create a script that deletes all files in the current working directory that end with the character `~`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/16-clean_emacs)
   * [Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/holberton` in the current directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/17-tree)
   * [Write a command that lists all the files and directories of the current directory, separated by commas (`,`).](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x00-shell_basics/18-commas)
     * Directory names should end with a slash (`/`)
     * Files and directories starting with a dot (`.`) should be listed
     * The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning
     * Only digits and letters are used to sort; Digits should come first
     * You can assume that all the files we will test with will have at least one letter or one digit
     * The listing should end with a new line
2. [Shell Permissions](https://github.com/srinitude/holbertonschool-sysadmin_devops/tree/master/0x01-shell_permissions)
   * [Create a script that changes your user ID to `betty`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/0-iam_betty)
     * You should use exactly 8 characters for your command (+1 character for the new line)
     * You can assume that the user `betty` will exist when we will run your script
   * [Write a script that prints the effective userid of the current user.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/1-who_am_i)
   * [Write a script that creates an empty file called `hello`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/4-empty)
   * [Write a script that prints all the groups the current user is part of.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/2-groups)
   * [Write a script that changes the owner of the file `hello` to the user `betty`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/3-new_owner)
   * [Write a script that adds execute permission to the owner of the file `hello`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/5-execute)
     * The file `hello` will be in the working directory
   * [Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/6-multiple_permissions)
     * The file `hello` will be in the working directory
   * [Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/7-everybody)
     * The file `hello` will be in the working directory
     * You are not allowed to use commas for this script
   * [Write a script that sets the permission to the file `hello` as follows:](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/8-James_Bond)
     * Owner: no permission at all
     * Group: no permission at all
     * Other users: all the permissions
     * The file `hello` will be in the working directory
     * You are not allowed to use commas for this script
   * [Write a script that sets the mode of the file `hello` to this:](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/9-John_Doe)
     ```
     -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
     ```
     * The file `hello` will be in the working directory
     * You are not allowed to use commas for this script
   * [Write a script that sets the mode of the file `hello` the same as `olleh`’s mode.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/10-mirror_permissions)
     * The file `hello` will be in the working directory
     * The file `olleh` will be in the working directory
     * Note: the mode of `olleh` will not always be 664. Make sure your script works for any mode.
   * [Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/11-directories_permissions)
   * [Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/12-directory_permissions)
   * [Write a script that changes the group owner to `holberton` for the file `hello`](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/13-change_group)
     * The file `hello` will be in the working directory
   * [Write a script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/14-change_owner_and_group)
   * [Write a script that changes the owner and the group owner of the file `_hello` to `betty` and `holberton` respectively.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/15-symbolic_link_permissions)
     * The file `_hello` is in the working directory
     * The file `_hello` is a symbolic link
   * [Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/16-if_only)
     * The file `hello` will be in the working directory
   * [Write a script that will play the StarWars IV episode in the terminal.](https://github.com/srinitude/holbertonschool-sysadmin_devops/blob/master/0x01-shell_permissions/100-Star_Wars)
3. [Shell Redirection](https://github.com/srinitude/holbertonschool-sysadmin_devops/tree/master/0x02-shell_redirections)
4. [Shell Variables and Expansion](https://github.com/srinitude/holbertonschool-sysadmin_devops/tree/master/0x03-shell_variables_expansions)