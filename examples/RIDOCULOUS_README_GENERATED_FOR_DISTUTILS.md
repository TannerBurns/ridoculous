- [ distutils.archive_util ](#distutils.archive_util_469901316)
- [ distutils.command.build_ext ](#distutils.command.build_ext_1163118793)
- [ distutils.cmd ](#distutils.cmd_230462319)
	- [ distutils.cmd.Command ](#distutils.cmd.Command_106075600)
		- [ Command.__getattr__ ](#Command.__getattr___337466095)
		- [ Command.__init__ ](#Command.__init___633910901)
		- [ Command._ensure_stringlike ](#Command._ensure_stringlike_867207524)
		- [ Command._ensure_tested_string ](#Command._ensure_tested_string_2122249873)
		- [ Command.announce ](#Command.announce_308777876)
		- [ Command.copy_file ](#Command.copy_file_862702987)
		- [ Command.copy_tree ](#Command.copy_tree_2027619881)
		- [ Command.debug_print ](#Command.debug_print_1136699583)
		- [ Command.dump_options ](#Command.dump_options_743102028)
		- [ Command.ensure_dirname ](#Command.ensure_dirname_1796042631)
		- [ Command.ensure_filename ](#Command.ensure_filename_2107133801)
		- [ Command.ensure_finalized ](#Command.ensure_finalized_1892422295)
		- [ Command.ensure_string ](#Command.ensure_string_1022270514)
		- [ Command.ensure_string_list ](#Command.ensure_string_list_1409267209)
		- [ Command.execute ](#Command.execute_1349113088)
		- [ Command.finalize_options ](#Command.finalize_options_714482464)
		- [ Command.get_command_name ](#Command.get_command_name_1348366013)
		- [ Command.get_finalized_command ](#Command.get_finalized_command_1903367791)
		- [ Command.get_sub_commands ](#Command.get_sub_commands_1202532609)
		- [ Command.initialize_options ](#Command.initialize_options_2043161938)
		- [ Command.make_archive ](#Command.make_archive_1822665747)
		- [ Command.make_file ](#Command.make_file_449286149)
		- [ Command.mkpath ](#Command.mkpath_1000491046)
		- [ Command.move_file ](#Command.move_file_1599603296)
		- [ Command.reinitialize_command ](#Command.reinitialize_command_1778384288)
		- [ Command.run ](#Command.run_1966546607)
		- [ Command.run_command ](#Command.run_command_408704732)
		- [ Command.set_undefined_options ](#Command.set_undefined_options_2016799020)
		- [ Command.spawn ](#Command.spawn_2007078989)
		- [ Command.warn ](#Command.warn_262463061)
- [ distutils.command ](#distutils.command_1842664969)
- [ distutils.config ](#distutils.config_1529948663)
	- [ distutils.config.PyPIRCCommand ](#distutils.config.PyPIRCCommand_1407719663)
		- [ PyPIRCCommand._get_rc_file ](#PyPIRCCommand._get_rc_file_1697312601)
		- [ PyPIRCCommand._read_pypi_response ](#PyPIRCCommand._read_pypi_response_2020601658)
		- [ PyPIRCCommand._read_pypirc ](#PyPIRCCommand._read_pypirc_1399518964)
		- [ PyPIRCCommand._store_pypirc ](#PyPIRCCommand._store_pypirc_629178429)
		- [ PyPIRCCommand.finalize_options ](#PyPIRCCommand.finalize_options_844633658)
		- [ PyPIRCCommand.initialize_options ](#PyPIRCCommand.initialize_options_42350140)
- [ distutils.core ](#distutils.core_666845015)
- [ distutils.debug ](#distutils.debug_2031569862)
- [ distutils.dep_util ](#distutils.dep_util_1657731668)
- [ distutils.dir_util ](#distutils.dir_util_1859052546)
- [ distutils.dist ](#distutils.dist_1442079341)
	- [ distutils.dist.Distribution ](#distutils.dist.Distribution_1586262874)
		- [ Distribution.__init__ ](#Distribution.__init___2021384862)
		- [ Distribution._get_toplevel_options ](#Distribution._get_toplevel_options_1138213062)
		- [ Distribution._parse_command_opts ](#Distribution._parse_command_opts_785603506)
		- [ Distribution._set_command_options ](#Distribution._set_command_options_132143607)
		- [ Distribution._show_help ](#Distribution._show_help_1689868733)
		- [ Distribution.announce ](#Distribution.announce_1644526770)
		- [ Distribution.dump_option_dicts ](#Distribution.dump_option_dicts_670589098)
		- [ Distribution.finalize_options ](#Distribution.finalize_options_57771697)
		- [ Distribution.get_command_class ](#Distribution.get_command_class_1444995109)
		- [ Distribution.get_command_list ](#Distribution.get_command_list_806131611)
		- [ Distribution.get_command_obj ](#Distribution.get_command_obj_787051391)
		- [ Distribution.get_command_packages ](#Distribution.get_command_packages_1876930807)
		- [ Distribution.get_option_dict ](#Distribution.get_option_dict_32473632)
		- [ Distribution.handle_display_options ](#Distribution.handle_display_options_1395475006)
		- [ Distribution.has_c_libraries ](#Distribution.has_c_libraries_2073702197)
		- [ Distribution.has_data_files ](#Distribution.has_data_files_482194422)
		- [ Distribution.has_ext_modules ](#Distribution.has_ext_modules_1766779142)
		- [ Distribution.has_headers ](#Distribution.has_headers_357446550)
		- [ Distribution.has_modules ](#Distribution.has_modules_721552444)
		- [ Distribution.has_pure_modules ](#Distribution.has_pure_modules_589428874)
		- [ Distribution.has_scripts ](#Distribution.has_scripts_1987363562)
		- [ Distribution.is_pure ](#Distribution.is_pure_1773774633)
		- [ Distribution.parse_command_line ](#Distribution.parse_command_line_1975797365)
		- [ Distribution.parse_config_files ](#Distribution.parse_config_files_1323525528)
		- [ Distribution.print_command_list ](#Distribution.print_command_list_1145297405)
		- [ Distribution.print_commands ](#Distribution.print_commands_1312430779)
		- [ Distribution.reinitialize_command ](#Distribution.reinitialize_command_1403515663)
		- [ Distribution.run_command ](#Distribution.run_command_927617509)
		- [ Distribution.run_commands ](#Distribution.run_commands_74359124)
	- [ distutils.dist.DistributionMetadata ](#distutils.dist.DistributionMetadata_422009319)
		- [ DistributionMetadata.__init__ ](#DistributionMetadata.__init___1365022953)
		- [ DistributionMetadata._write_list ](#DistributionMetadata._write_list_1468236717)
		- [ DistributionMetadata.get_author ](#DistributionMetadata.get_author_352220947)
		- [ DistributionMetadata.get_author_email ](#DistributionMetadata.get_author_email_1024769200)
		- [ DistributionMetadata.get_classifiers ](#DistributionMetadata.get_classifiers_2016138068)
		- [ DistributionMetadata.get_contact ](#DistributionMetadata.get_contact_550985507)
		- [ DistributionMetadata.get_contact_email ](#DistributionMetadata.get_contact_email_246311614)
		- [ DistributionMetadata.get_description ](#DistributionMetadata.get_description_1300836878)
		- [ DistributionMetadata.get_download_url ](#DistributionMetadata.get_download_url_710147159)
		- [ DistributionMetadata.get_fullname ](#DistributionMetadata.get_fullname_1081107921)
		- [ DistributionMetadata.get_keywords ](#DistributionMetadata.get_keywords_2067289902)
		- [ DistributionMetadata.get_license ](#DistributionMetadata.get_license_197576525)
		- [ DistributionMetadata.get_license ](#DistributionMetadata.get_license_197576525)
		- [ DistributionMetadata.get_long_description ](#DistributionMetadata.get_long_description_1256244935)
		- [ DistributionMetadata.get_maintainer ](#DistributionMetadata.get_maintainer_1453792752)
		- [ DistributionMetadata.get_maintainer_email ](#DistributionMetadata.get_maintainer_email_1530910385)
		- [ DistributionMetadata.get_name ](#DistributionMetadata.get_name_1662836324)
		- [ DistributionMetadata.get_obsoletes ](#DistributionMetadata.get_obsoletes_1325941508)
		- [ DistributionMetadata.get_platforms ](#DistributionMetadata.get_platforms_1438638502)
		- [ DistributionMetadata.get_provides ](#DistributionMetadata.get_provides_965753545)
		- [ DistributionMetadata.get_requires ](#DistributionMetadata.get_requires_591315055)
		- [ DistributionMetadata.get_url ](#DistributionMetadata.get_url_617534023)
		- [ DistributionMetadata.get_version ](#DistributionMetadata.get_version_1068735831)
		- [ DistributionMetadata.read_pkg_file ](#DistributionMetadata.read_pkg_file_412404660)
		- [ DistributionMetadata.set_classifiers ](#DistributionMetadata.set_classifiers_251974143)
		- [ DistributionMetadata.set_keywords ](#DistributionMetadata.set_keywords_2025347448)
		- [ DistributionMetadata.set_obsoletes ](#DistributionMetadata.set_obsoletes_623153967)
		- [ DistributionMetadata.set_platforms ](#DistributionMetadata.set_platforms_1772322636)
		- [ DistributionMetadata.set_provides ](#DistributionMetadata.set_provides_1471560459)
		- [ DistributionMetadata.set_requires ](#DistributionMetadata.set_requires_454021952)
		- [ DistributionMetadata.write_pkg_file ](#DistributionMetadata.write_pkg_file_632399158)
		- [ DistributionMetadata.write_pkg_info ](#DistributionMetadata.write_pkg_info_1457307811)
- [ distutils.errors ](#distutils.errors_1477621062)
	- [ distutils.errors.CCompilerError ](#distutils.errors.CCompilerError_1156007540)
	- [ distutils.errors.CompileError ](#distutils.errors.CompileError_1204767230)
	- [ distutils.errors.DistutilsArgError ](#distutils.errors.DistutilsArgError_656927888)
	- [ distutils.errors.DistutilsByteCompileError ](#distutils.errors.DistutilsByteCompileError_1499025797)
	- [ distutils.errors.DistutilsClassError ](#distutils.errors.DistutilsClassError_494291113)
	- [ distutils.errors.DistutilsError ](#distutils.errors.DistutilsError_1617462357)
	- [ distutils.errors.DistutilsExecError ](#distutils.errors.DistutilsExecError_2124089141)
	- [ distutils.errors.DistutilsFileError ](#distutils.errors.DistutilsFileError_537118856)
	- [ distutils.errors.DistutilsGetoptError ](#distutils.errors.DistutilsGetoptError_1665518692)
	- [ distutils.errors.DistutilsInternalError ](#distutils.errors.DistutilsInternalError_1262974833)
	- [ distutils.errors.DistutilsModuleError ](#distutils.errors.DistutilsModuleError_256279945)
	- [ distutils.errors.DistutilsOptionError ](#distutils.errors.DistutilsOptionError_1744360067)
	- [ distutils.errors.DistutilsPlatformError ](#distutils.errors.DistutilsPlatformError_1448920055)
	- [ distutils.errors.DistutilsSetupError ](#distutils.errors.DistutilsSetupError_145050882)
	- [ distutils.errors.DistutilsTemplateError ](#distutils.errors.DistutilsTemplateError_383922332)
	- [ distutils.errors.LibError ](#distutils.errors.LibError_2113512248)
	- [ distutils.errors.LinkError ](#distutils.errors.LinkError_796111847)
	- [ distutils.errors.PreprocessError ](#distutils.errors.PreprocessError_1345931261)
	- [ distutils.errors.UnknownFileError ](#distutils.errors.UnknownFileError_868119557)
- [ distutils.extension ](#distutils.extension_599566899)
	- [ distutils.extension.Extension ](#distutils.extension.Extension_787829314)
		- [ Extension.__init__ ](#Extension.__init___1296968659)
		- [ Extension.__repr__ ](#Extension.__repr___2023873679)
- [ distutils.fancy_getopt ](#distutils.fancy_getopt_310386000)
	- [ distutils.fancy_getopt.FancyGetopt ](#distutils.fancy_getopt.FancyGetopt_730766271)
		- [ FancyGetopt.__init__ ](#FancyGetopt.__init___391453862)
		- [ FancyGetopt._build_index ](#FancyGetopt._build_index_1444118159)
		- [ FancyGetopt._check_alias_dict ](#FancyGetopt._check_alias_dict_118328429)
		- [ FancyGetopt._grok_option_table ](#FancyGetopt._grok_option_table_979055245)
		- [ FancyGetopt.add_option ](#FancyGetopt.add_option_995751347)
		- [ FancyGetopt.generate_help ](#FancyGetopt.generate_help_1026363145)
		- [ FancyGetopt.get_attr_name ](#FancyGetopt.get_attr_name_415219163)
		- [ FancyGetopt.get_option_order ](#FancyGetopt.get_option_order_514337364)
		- [ FancyGetopt.getopt ](#FancyGetopt.getopt_294991514)
		- [ FancyGetopt.has_option ](#FancyGetopt.has_option_408185363)
		- [ FancyGetopt.print_help ](#FancyGetopt.print_help_1103953632)
		- [ FancyGetopt.set_aliases ](#FancyGetopt.set_aliases_1810892686)
		- [ FancyGetopt.set_negative_aliases ](#FancyGetopt.set_negative_aliases_749037856)
		- [ FancyGetopt.set_option_table ](#FancyGetopt.set_option_table_1853321417)
	- [ distutils.fancy_getopt.OptionDummy ](#distutils.fancy_getopt.OptionDummy_22597836)
		- [ OptionDummy.__init__ ](#OptionDummy.__init___205744830)
- [ distutils.file_util ](#distutils.file_util_424009387)
- [ distutils.log ](#distutils.log_727395436)
	- [ distutils.log.Log ](#distutils.log.Log_723538835)
		- [ Log.__init__ ](#Log.__init___783981344)
		- [ Log._log ](#Log._log_1895113537)
		- [ Log.debug ](#Log.debug_154216507)
		- [ Log.error ](#Log.error_1223014898)
		- [ Log.fatal ](#Log.fatal_1141627102)
		- [ Log.info ](#Log.info_128364290)
		- [ Log.log ](#Log.log_1397817601)
		- [ Log.warn ](#Log.warn_625023016)
- [ _virtualenv_distutils ](#_virtualenv_distutils_1884558016)
- [ distutils.spawn ](#distutils.spawn_381508274)
- [ distutils.sysconfig ](#distutils.sysconfig_1670193064)
- [ distutils.util ](#distutils.util_407928641)
	- [ distutils.util.Mixin2to3 ](#distutils.util.Mixin2to3_551833640)
		- [ Mixin2to3.run_2to3 ](#Mixin2to3.run_2to3_1226325292)

<a name="distutils.archive_util_469901316"></a>
## distutils.archive_util

<a name="distutils.command.build_ext_1163118793"></a>
## distutils.command.build_ext

<a name="distutils.cmd_230462319"></a>
## distutils.cmd

<a name="distutils.cmd.Command_106075600"></a>
### distutils.cmd.Command(self, dist)

Abstract base class for defining command classes, the "worker bees"
    of the Distutils.  A useful analogy for command classes is to think of
    them as subroutines with local variables called "options".  The options
    are "declared" in 'initialize_options()' and "defined" (given their
    final values, aka "finalized") in 'finalize_options()', both of which
    must be defined by every command class.  The distinction between the
    two is necessary because option values might come from the outside
    world (command line, config file, ...), and any options dependent on
    other options must be computed *after* these outside influences have
    been processed -- hence 'finalize_options()'.  The "body" of the
    subroutine, where it does all its work based on the values of its
    options, is the 'run()' method, which must also be implemented by every
    command class.
    

<a name="Command.__getattr___337466095"></a>
#### `Command.__getattr__(self, attr)`

None

<a name="Command.__init___633910901"></a>
#### `Command.__init__(self, dist)`

Create and initialize a new Command object.  Most importantly,
        invokes the 'initialize_options()' method, which is the real
        initializer and depends on the actual command being
        instantiated.
        

<a name="Command._ensure_stringlike_867207524"></a>
#### `Command._ensure_stringlike(self, option, what, default=None)`

None

<a name="Command._ensure_tested_string_2122249873"></a>
#### `Command._ensure_tested_string(self, option, tester, what, error_fmt, default=None)`

None

<a name="Command.announce_308777876"></a>
#### `Command.announce(self, msg, level=1)`

If the current verbosity level is of greater than or equal to
        'level' print 'msg' to stdout.
        

<a name="Command.copy_file_862702987"></a>
#### `Command.copy_file(self, infile, outfile, preserve_mode=1, preserve_times=1, link=None, level=1)`

Copy a file respecting verbose, dry-run and force flags.  (The
        former two default to whatever is in the Distribution object, and
        the latter defaults to false for commands that don't define it.)

<a name="Command.copy_tree_2027619881"></a>
#### `Command.copy_tree(self, infile, outfile, preserve_mode=1, preserve_times=1, preserve_symlinks=0, level=1)`

Copy an entire directory tree respecting verbose, dry-run,
        and force flags.
        

<a name="Command.debug_print_1136699583"></a>
#### `Command.debug_print(self, msg)`

Print 'msg' to stdout if the global DEBUG (taken from the
        DISTUTILS_DEBUG environment variable) flag is true.
        

<a name="Command.dump_options_743102028"></a>
#### `Command.dump_options(self, header=None, indent='')`

None

<a name="Command.ensure_dirname_1796042631"></a>
#### `Command.ensure_dirname(self, option)`

None

<a name="Command.ensure_filename_2107133801"></a>
#### `Command.ensure_filename(self, option)`

Ensure that 'option' is the name of an existing file.

<a name="Command.ensure_finalized_1892422295"></a>
#### `Command.ensure_finalized(self)`

None

<a name="Command.ensure_string_1022270514"></a>
#### `Command.ensure_string(self, option, default=None)`

Ensure that 'option' is a string; if not defined, set it to
        'default'.
        

<a name="Command.ensure_string_list_1409267209"></a>
#### `Command.ensure_string_list(self, option)`

Ensure that 'option' is a list of strings.  If 'option' is
        currently a string, we split it either on /,\s*/ or /\s+/, so
        "foo bar baz", "foo,bar,baz", and "foo,   bar baz" all become
        ["foo", "bar", "baz"].
        

<a name="Command.execute_1349113088"></a>
#### `Command.execute(self, func, args, msg=None, level=1)`

None

<a name="Command.finalize_options_714482464"></a>
#### `Command.finalize_options(self)`

Set final values for all the options that this command supports.
        This is always called as late as possible, ie.  after any option
        assignments from the command-line or from other commands have been
        done.  Thus, this is the place to code option dependencies: if
        'foo' depends on 'bar', then it is safe to set 'foo' from 'bar' as
        long as 'foo' still has the same value it was assigned in
        'initialize_options()'.

        This method must be implemented by all command classes.
        

<a name="Command.get_command_name_1348366013"></a>
#### `Command.get_command_name(self)`

None

<a name="Command.get_finalized_command_1903367791"></a>
#### `Command.get_finalized_command(self, command, create=1)`

Wrapper around Distribution's 'get_command_obj()' method: find
        (create if necessary and 'create' is true) the command object for
        'command', call its 'ensure_finalized()' method, and return the
        finalized command object.
        

<a name="Command.get_sub_commands_1202532609"></a>
#### `Command.get_sub_commands(self)`

Determine the sub-commands that are relevant in the current
        distribution (ie., that need to be run).  This is based on the
        'sub_commands' class attribute: each tuple in that list may include
        a method that we call to determine if the subcommand needs to be
        run for the current distribution.  Return a list of command names.
        

<a name="Command.initialize_options_2043161938"></a>
#### `Command.initialize_options(self)`

Set default values for all the options that this command
        supports.  Note that these defaults may be overridden by other
        commands, by the setup script, by config files, or by the
        command-line.  Thus, this is not the place to code dependencies
        between options; generally, 'initialize_options()' implementations
        are just a bunch of "self.foo = None" assignments.

        This method must be implemented by all command classes.
        

<a name="Command.make_archive_1822665747"></a>
#### `Command.make_archive(self, base_name, format, root_dir=None, base_dir=None, owner=None, group=None)`

None

<a name="Command.make_file_449286149"></a>
#### `Command.make_file(self, infiles, outfile, func, args, exec_msg=None, skip_msg=None, level=1)`

Special case of 'execute()' for operations that process one or
        more input files and generate one output file.  Works just like
        'execute()', except the operation is skipped and a different
        message printed if 'outfile' already exists and is newer than all
        files listed in 'infiles'.  If the command defined 'self.force',
        and it is true, then the command is unconditionally run -- does no
        timestamp checks.
        

<a name="Command.mkpath_1000491046"></a>
#### `Command.mkpath(self, name, mode=511)`

None

<a name="Command.move_file_1599603296"></a>
#### `Command.move_file(self, src, dst, level=1)`

Move a file respecting dry-run flag.

<a name="Command.reinitialize_command_1778384288"></a>
#### `Command.reinitialize_command(self, command, reinit_subcommands=0)`

None

<a name="Command.run_1966546607"></a>
#### `Command.run(self)`

A command's raison d'etre: carry out the action it exists to
        perform, controlled by the options initialized in
        'initialize_options()', customized by other commands, the setup
        script, the command-line, and config files, and finalized in
        'finalize_options()'.  All terminal output and filesystem
        interaction should be done by 'run()'.

        This method must be implemented by all command classes.
        

<a name="Command.run_command_408704732"></a>
#### `Command.run_command(self, command)`

Run some other command: uses the 'run_command()' method of
        Distribution, which creates and finalizes the command object if
        necessary and then invokes its 'run()' method.
        

<a name="Command.set_undefined_options_2016799020"></a>
#### `Command.set_undefined_options(self, src_cmd, *option_pairs)`

Set the values of any "undefined" options from corresponding
        option values in some other command object.  "Undefined" here means
        "is None", which is the convention used to indicate that an option
        has not been changed between 'initialize_options()' and
        'finalize_options()'.  Usually called from 'finalize_options()' for
        options that depend on some other command rather than another
        option of the same command.  'src_cmd' is the other command from
        which option values will be taken (a command object will be created
        for it if necessary); the remaining arguments are
        '(src_option,dst_option)' tuples which mean "take the value of
        'src_option' in the 'src_cmd' command object, and copy it to
        'dst_option' in the current command object".
        

<a name="Command.spawn_2007078989"></a>
#### `Command.spawn(self, cmd, search_path=1, level=1)`

Spawn an external command respecting dry-run flag.

<a name="Command.warn_262463061"></a>
#### `Command.warn(self, msg)`

None

<a name="distutils.command_1842664969"></a>
## distutils.command

<a name="distutils.config_1529948663"></a>
## distutils.config

<a name="distutils.config.PyPIRCCommand_1407719663"></a>
### distutils.config.PyPIRCCommand(self, dist)

Base command that knows how to handle the .pypirc file
    

<a name="PyPIRCCommand._get_rc_file_1697312601"></a>
#### `PyPIRCCommand._get_rc_file(self)`

Returns rc file path.

<a name="PyPIRCCommand._read_pypi_response_2020601658"></a>
#### `PyPIRCCommand._read_pypi_response(self, response)`

Read and decode a PyPI HTTP response.

<a name="PyPIRCCommand._read_pypirc_1399518964"></a>
#### `PyPIRCCommand._read_pypirc(self)`

Reads the .pypirc file.

<a name="PyPIRCCommand._store_pypirc_629178429"></a>
#### `PyPIRCCommand._store_pypirc(self, username, password)`

Creates a default .pypirc file.

<a name="PyPIRCCommand.finalize_options_844633658"></a>
#### `PyPIRCCommand.finalize_options(self)`

Finalizes options.

<a name="PyPIRCCommand.initialize_options_42350140"></a>
#### `PyPIRCCommand.initialize_options(self)`

Initialize options.

<a name="distutils.core_666845015"></a>
## distutils.core

<a name="distutils.debug_2031569862"></a>
## distutils.debug

<a name="distutils.dep_util_1657731668"></a>
## distutils.dep_util

<a name="distutils.dir_util_1859052546"></a>
## distutils.dir_util

<a name="distutils.dist_1442079341"></a>
## distutils.dist

<a name="distutils.dist.Distribution_1586262874"></a>
### distutils.dist.Distribution(self, attrs=None)

The core of the Distutils.  Most of the work hiding behind 'setup'
    is really done within a Distribution instance, which farms the work out
    to the Distutils commands specified on the command line.

    Setup scripts will almost never instantiate Distribution directly,
    unless the 'setup()' function is totally inadequate to their needs.
    However, it is conceivable that a setup script might wish to subclass
    Distribution for some specialized purpose, and then pass the subclass
    to 'setup()' as the 'distclass' keyword argument.  If so, it is
    necessary to respect the expectations that 'setup' has of Distribution.
    See the code for 'setup()', in core.py, for details.
    

<a name="Distribution.__init___2021384862"></a>
#### `Distribution.__init__(self, attrs=None)`

Construct a new Distribution instance: initialize all the
        attributes of a Distribution, and then use 'attrs' (a dictionary
        mapping attribute names to values) to assign some of those
        attributes their "real" values.  (Any attributes not mentioned in
        'attrs' will be assigned to some null value: 0, None, an empty list
        or dictionary, etc.)  Most importantly, initialize the
        'command_obj' attribute to the empty dictionary; this will be
        filled in with real command objects by 'parse_command_line()'.
        

<a name="Distribution._get_toplevel_options_1138213062"></a>
#### `Distribution._get_toplevel_options(self)`

Return the non-display options recognized at the top level.

        This includes options that are recognized *only* at the top
        level as well as options recognized for commands.
        

<a name="Distribution._parse_command_opts_785603506"></a>
#### `Distribution._parse_command_opts(self, parser, args)`

Parse the command-line options for a single command.
        'parser' must be a FancyGetopt instance; 'args' must be the list
        of arguments, starting with the current command (whose options
        we are about to parse).  Returns a new version of 'args' with
        the next command at the front of the list; will be the empty
        list if there are no more commands on the command line.  Returns
        None if the user asked for help on this command.
        

<a name="Distribution._set_command_options_132143607"></a>
#### `Distribution._set_command_options(self, command_obj, option_dict=None)`

Set the options for 'command_obj' from 'option_dict'.  Basically
        this means copying elements of a dictionary ('option_dict') to
        attributes of an instance ('command').

        'command_obj' must be a Command instance.  If 'option_dict' is not
        supplied, uses the standard option dictionary for this command
        (from 'self.command_options').
        

<a name="Distribution._show_help_1689868733"></a>
#### `Distribution._show_help(self, parser, global_options=1, display_options=1, commands=[])`

Show help for the setup script command-line in the form of
        several lists of command-line options.  'parser' should be a
        FancyGetopt instance; do not expect it to be returned in the
        same state, as its option table will be reset to make it
        generate the correct help text.

        If 'global_options' is true, lists the global options:
        --verbose, --dry-run, etc.  If 'display_options' is true, lists
        the "display-only" options: --name, --version, etc.  Finally,
        lists per-command help for every command name or command class
        in 'commands'.
        

<a name="Distribution.announce_1644526770"></a>
#### `Distribution.announce(self, msg, level=2)`

None

<a name="Distribution.dump_option_dicts_670589098"></a>
#### `Distribution.dump_option_dicts(self, header=None, commands=None, indent='')`

None

<a name="Distribution.finalize_options_57771697"></a>
#### `Distribution.finalize_options(self)`

Set final values for all the options on the Distribution
        instance, analogous to the .finalize_options() method of Command
        objects.
        

<a name="Distribution.get_command_class_1444995109"></a>
#### `Distribution.get_command_class(self, command)`

Return the class that implements the Distutils command named by
        'command'.  First we check the 'cmdclass' dictionary; if the
        command is mentioned there, we fetch the class object from the
        dictionary and return it.  Otherwise we load the command module
        ("distutils.command." + command) and fetch the command class from
        the module.  The loaded class is also stored in 'cmdclass'
        to speed future calls to 'get_command_class()'.

        Raises DistutilsModuleError if the expected module could not be
        found, or if that module does not define the expected class.
        

<a name="Distribution.get_command_list_806131611"></a>
#### `Distribution.get_command_list(self)`

Get a list of (command, description) tuples.
        The list is divided into "standard commands" (listed in
        distutils.command.__all__) and "extra commands" (mentioned in
        self.cmdclass, but not a standard command).  The descriptions come
        from the command class attribute 'description'.
        

<a name="Distribution.get_command_obj_787051391"></a>
#### `Distribution.get_command_obj(self, command, create=1)`

Return the command object for 'command'.  Normally this object
        is cached on a previous call to 'get_command_obj()'; if no command
        object for 'command' is in the cache, then we either create and
        return it (if 'create' is true) or return None.
        

<a name="Distribution.get_command_packages_1876930807"></a>
#### `Distribution.get_command_packages(self)`

Return a list of packages from which commands are loaded.

<a name="Distribution.get_option_dict_32473632"></a>
#### `Distribution.get_option_dict(self, command)`

Get the option dictionary for a given command.  If that
        command's option dictionary hasn't been created yet, then create it
        and return the new dictionary; otherwise, return the existing
        option dictionary.
        

<a name="Distribution.handle_display_options_1395475006"></a>
#### `Distribution.handle_display_options(self, option_order)`

If there were any non-global "display-only" options
        (--help-commands or the metadata display options) on the command
        line, display the requested info and return true; else return
        false.
        

<a name="Distribution.has_c_libraries_2073702197"></a>
#### `Distribution.has_c_libraries(self)`

None

<a name="Distribution.has_data_files_482194422"></a>
#### `Distribution.has_data_files(self)`

None

<a name="Distribution.has_ext_modules_1766779142"></a>
#### `Distribution.has_ext_modules(self)`

None

<a name="Distribution.has_headers_357446550"></a>
#### `Distribution.has_headers(self)`

None

<a name="Distribution.has_modules_721552444"></a>
#### `Distribution.has_modules(self)`

None

<a name="Distribution.has_pure_modules_589428874"></a>
#### `Distribution.has_pure_modules(self)`

None

<a name="Distribution.has_scripts_1987363562"></a>
#### `Distribution.has_scripts(self)`

None

<a name="Distribution.is_pure_1773774633"></a>
#### `Distribution.is_pure(self)`

None

<a name="Distribution.parse_command_line_1975797365"></a>
#### `Distribution.parse_command_line(self)`

Parse the setup script's command line, taken from the
        'script_args' instance attribute (which defaults to 'sys.argv[1:]'
        -- see 'setup()' in core.py).  This list is first processed for
        "global options" -- options that set attributes of the Distribution
        instance.  Then, it is alternately scanned for Distutils commands
        and options for that command.  Each new command terminates the
        options for the previous command.  The allowed options for a
        command are determined by the 'user_options' attribute of the
        command class -- thus, we have to be able to load command classes
        in order to parse the command line.  Any error in that 'options'
        attribute raises DistutilsGetoptError; any error on the
        command-line raises DistutilsArgError.  If no Distutils commands
        were found on the command line, raises DistutilsArgError.  Return
        true if command-line was successfully parsed and we should carry
        on with executing commands; false if no errors but we shouldn't
        execute commands (currently, this only happens if user asks for
        help).
        

<a name="Distribution.parse_config_files_1323525528"></a>
#### `Distribution.parse_config_files(self, filenames=None)`

None

<a name="Distribution.print_command_list_1145297405"></a>
#### `Distribution.print_command_list(self, commands, header, max_length)`

Print a subset of the list of all commands -- used by
        'print_commands()'.
        

<a name="Distribution.print_commands_1312430779"></a>
#### `Distribution.print_commands(self)`

Print out a help message listing all available commands with a
        description of each.  The list is divided into "standard commands"
        (listed in distutils.command.__all__) and "extra commands"
        (mentioned in self.cmdclass, but not a standard command).  The
        descriptions come from the command class attribute
        'description'.
        

<a name="Distribution.reinitialize_command_1403515663"></a>
#### `Distribution.reinitialize_command(self, command, reinit_subcommands=0)`

Reinitializes a command to the state it was in when first
        returned by 'get_command_obj()': ie., initialized but not yet
        finalized.  This provides the opportunity to sneak option
        values in programmatically, overriding or supplementing
        user-supplied values from the config files and command line.
        You'll have to re-finalize the command object (by calling
        'finalize_options()' or 'ensure_finalized()') before using it for
        real.

        'command' should be a command name (string) or command object.  If
        'reinit_subcommands' is true, also reinitializes the command's
        sub-commands, as declared by the 'sub_commands' class attribute (if
        it has one).  See the "install" command for an example.  Only
        reinitializes the sub-commands that actually matter, ie. those
        whose test predicates return true.

        Returns the reinitialized command object.
        

<a name="Distribution.run_command_927617509"></a>
#### `Distribution.run_command(self, command)`

Do whatever it takes to run a command (including nothing at all,
        if the command has already been run).  Specifically: if we have
        already created and run the command named by 'command', return
        silently without doing anything.  If the command named by 'command'
        doesn't even have a command object yet, create one.  Then invoke
        'run()' on that command object (or an existing one).
        

<a name="Distribution.run_commands_74359124"></a>
#### `Distribution.run_commands(self)`

Run each command that was seen on the setup script command line.
        Uses the list of commands found and cache of command objects
        created by 'get_command_obj()'.
        

<a name="distutils.dist.DistributionMetadata_422009319"></a>
### distutils.dist.DistributionMetadata(self, path=None)

Dummy class to hold the distribution meta-data: name, version,
    author, and so forth.
    

<a name="DistributionMetadata.__init___1365022953"></a>
#### `DistributionMetadata.__init__(self, path=None)`

None

<a name="DistributionMetadata._write_list_1468236717"></a>
#### `DistributionMetadata._write_list(self, file, name, values)`

None

<a name="DistributionMetadata.get_author_352220947"></a>
#### `DistributionMetadata.get_author(self)`

None

<a name="DistributionMetadata.get_author_email_1024769200"></a>
#### `DistributionMetadata.get_author_email(self)`

None

<a name="DistributionMetadata.get_classifiers_2016138068"></a>
#### `DistributionMetadata.get_classifiers(self)`

None

<a name="DistributionMetadata.get_contact_550985507"></a>
#### `DistributionMetadata.get_contact(self)`

None

<a name="DistributionMetadata.get_contact_email_246311614"></a>
#### `DistributionMetadata.get_contact_email(self)`

None

<a name="DistributionMetadata.get_description_1300836878"></a>
#### `DistributionMetadata.get_description(self)`

None

<a name="DistributionMetadata.get_download_url_710147159"></a>
#### `DistributionMetadata.get_download_url(self)`

None

<a name="DistributionMetadata.get_fullname_1081107921"></a>
#### `DistributionMetadata.get_fullname(self)`

None

<a name="DistributionMetadata.get_keywords_2067289902"></a>
#### `DistributionMetadata.get_keywords(self)`

None

<a name="DistributionMetadata.get_license_197576525"></a>
#### `DistributionMetadata.get_license(self)`

None

<a name="DistributionMetadata.get_license_197576525"></a>
#### `DistributionMetadata.get_license(self)`

None

<a name="DistributionMetadata.get_long_description_1256244935"></a>
#### `DistributionMetadata.get_long_description(self)`

None

<a name="DistributionMetadata.get_maintainer_1453792752"></a>
#### `DistributionMetadata.get_maintainer(self)`

None

<a name="DistributionMetadata.get_maintainer_email_1530910385"></a>
#### `DistributionMetadata.get_maintainer_email(self)`

None

<a name="DistributionMetadata.get_name_1662836324"></a>
#### `DistributionMetadata.get_name(self)`

None

<a name="DistributionMetadata.get_obsoletes_1325941508"></a>
#### `DistributionMetadata.get_obsoletes(self)`

None

<a name="DistributionMetadata.get_platforms_1438638502"></a>
#### `DistributionMetadata.get_platforms(self)`

None

<a name="DistributionMetadata.get_provides_965753545"></a>
#### `DistributionMetadata.get_provides(self)`

None

<a name="DistributionMetadata.get_requires_591315055"></a>
#### `DistributionMetadata.get_requires(self)`

None

<a name="DistributionMetadata.get_url_617534023"></a>
#### `DistributionMetadata.get_url(self)`

None

<a name="DistributionMetadata.get_version_1068735831"></a>
#### `DistributionMetadata.get_version(self)`

None

<a name="DistributionMetadata.read_pkg_file_412404660"></a>
#### `DistributionMetadata.read_pkg_file(self, file)`

Reads the metadata values from a file object.

<a name="DistributionMetadata.set_classifiers_251974143"></a>
#### `DistributionMetadata.set_classifiers(self, value)`

None

<a name="DistributionMetadata.set_keywords_2025347448"></a>
#### `DistributionMetadata.set_keywords(self, value)`

None

<a name="DistributionMetadata.set_obsoletes_623153967"></a>
#### `DistributionMetadata.set_obsoletes(self, value)`

None

<a name="DistributionMetadata.set_platforms_1772322636"></a>
#### `DistributionMetadata.set_platforms(self, value)`

None

<a name="DistributionMetadata.set_provides_1471560459"></a>
#### `DistributionMetadata.set_provides(self, value)`

None

<a name="DistributionMetadata.set_requires_454021952"></a>
#### `DistributionMetadata.set_requires(self, value)`

None

<a name="DistributionMetadata.write_pkg_file_632399158"></a>
#### `DistributionMetadata.write_pkg_file(self, file)`

Write the PKG-INFO format data to a file object.
        

<a name="DistributionMetadata.write_pkg_info_1457307811"></a>
#### `DistributionMetadata.write_pkg_info(self, base_dir)`

Write the PKG-INFO file into the release tree.
        

<a name="distutils.errors_1477621062"></a>
## distutils.errors

<a name="distutils.errors.CCompilerError_1156007540"></a>
### distutils.errors.CCompilerError(self, /, *args, **kwargs)

Some compile/link operation failed.

<a name="distutils.errors.CompileError_1204767230"></a>
### distutils.errors.CompileError(self, /, *args, **kwargs)

Failure to compile one or more C/C++ source files.

<a name="distutils.errors.DistutilsArgError_656927888"></a>
### distutils.errors.DistutilsArgError(self, /, *args, **kwargs)

Raised by fancy_getopt in response to getopt.error -- ie. an
    error in the command line usage.

<a name="distutils.errors.DistutilsByteCompileError_1499025797"></a>
### distutils.errors.DistutilsByteCompileError(self, /, *args, **kwargs)

Byte compile error.

<a name="distutils.errors.DistutilsClassError_494291113"></a>
### distutils.errors.DistutilsClassError(self, /, *args, **kwargs)

Some command class (or possibly distribution class, if anyone
    feels a need to subclass Distribution) is found not to be holding
    up its end of the bargain, ie. implementing some part of the
    "command "interface.

<a name="distutils.errors.DistutilsError_1617462357"></a>
### distutils.errors.DistutilsError(self, /, *args, **kwargs)

The root of all Distutils evil.

<a name="distutils.errors.DistutilsExecError_2124089141"></a>
### distutils.errors.DistutilsExecError(self, /, *args, **kwargs)

Any problems executing an external program (such as the C
    compiler, when compiling C files).

<a name="distutils.errors.DistutilsFileError_537118856"></a>
### distutils.errors.DistutilsFileError(self, /, *args, **kwargs)

Any problems in the filesystem: expected file not found, etc.
    Typically this is for problems that we detect before OSError
    could be raised.

<a name="distutils.errors.DistutilsGetoptError_1665518692"></a>
### distutils.errors.DistutilsGetoptError(self, /, *args, **kwargs)

The option table provided to 'fancy_getopt()' is bogus.

<a name="distutils.errors.DistutilsInternalError_1262974833"></a>
### distutils.errors.DistutilsInternalError(self, /, *args, **kwargs)

Internal inconsistencies or impossibilities (obviously, this
    should never be seen if the code is working!).

<a name="distutils.errors.DistutilsModuleError_256279945"></a>
### distutils.errors.DistutilsModuleError(self, /, *args, **kwargs)

Unable to load an expected module, or to find an expected class
    within some module (in particular, command modules and classes).

<a name="distutils.errors.DistutilsOptionError_1744360067"></a>
### distutils.errors.DistutilsOptionError(self, /, *args, **kwargs)

Syntactic/semantic errors in command options, such as use of
    mutually conflicting options, or inconsistent options,
    badly-spelled values, etc.  No distinction is made between option
    values originating in the setup script, the command line, config
    files, or what-have-you -- but if we *know* something originated in
    the setup script, we'll raise DistutilsSetupError instead.

<a name="distutils.errors.DistutilsPlatformError_1448920055"></a>
### distutils.errors.DistutilsPlatformError(self, /, *args, **kwargs)

We don't know how to do something on the current platform (but
    we do know how to do it on some platform) -- eg. trying to compile
    C files on a platform not supported by a CCompiler subclass.

<a name="distutils.errors.DistutilsSetupError_145050882"></a>
### distutils.errors.DistutilsSetupError(self, /, *args, **kwargs)

For errors that can be definitely blamed on the setup script,
    such as invalid keyword arguments to 'setup()'.

<a name="distutils.errors.DistutilsTemplateError_383922332"></a>
### distutils.errors.DistutilsTemplateError(self, /, *args, **kwargs)

Syntax error in a file list template.

<a name="distutils.errors.LibError_2113512248"></a>
### distutils.errors.LibError(self, /, *args, **kwargs)

Failure to create a static library from one or more C/C++ object
    files.

<a name="distutils.errors.LinkError_796111847"></a>
### distutils.errors.LinkError(self, /, *args, **kwargs)

Failure to link one or more C/C++ object files into an executable
    or shared library file.

<a name="distutils.errors.PreprocessError_1345931261"></a>
### distutils.errors.PreprocessError(self, /, *args, **kwargs)

Failure to preprocess one or more C/C++ files.

<a name="distutils.errors.UnknownFileError_868119557"></a>
### distutils.errors.UnknownFileError(self, /, *args, **kwargs)

Attempt to process an unknown file type.

<a name="distutils.extension_599566899"></a>
## distutils.extension

<a name="distutils.extension.Extension_787829314"></a>
### distutils.extension.Extension(self, name, sources, include_dirs=None, define_macros=None, undef_macros=None, library_dirs=None, libraries=None, runtime_library_dirs=None, extra_objects=None, extra_compile_args=None, extra_link_args=None, export_symbols=None, swig_opts=None, depends=None, language=None, optional=None, **kw)

Just a collection of attributes that describes an extension
    module and everything needed to build it (hopefully in a portable
    way, but there are hooks that let you be as unportable as you need).

    Instance attributes:
      name : string
        the full name of the extension, including any packages -- ie.
        *not* a filename or pathname, but Python dotted name
      sources : [string]
        list of source filenames, relative to the distribution root
        (where the setup script lives), in Unix form (slash-separated)
        for portability.  Source files may be C, C++, SWIG (.i),
        platform-specific resource files, or whatever else is recognized
        by the "build_ext" command as source for a Python extension.
      include_dirs : [string]
        list of directories to search for C/C++ header files (in Unix
        form for portability)
      define_macros : [(name : string, value : string|None)]
        list of macros to define; each macro is defined using a 2-tuple,
        where 'value' is either the string to define it to or None to
        define it without a particular value (equivalent of "#define
        FOO" in source or -DFOO on Unix C compiler command line)
      undef_macros : [string]
        list of macros to undefine explicitly
      library_dirs : [string]
        list of directories to search for C/C++ libraries at link time
      libraries : [string]
        list of library names (not filenames or paths) to link against
      runtime_library_dirs : [string]
        list of directories to search for C/C++ libraries at run time
        (for shared extensions, this is when the extension is loaded)
      extra_objects : [string]
        list of extra files to link with (eg. object files not implied
        by 'sources', static library that must be explicitly specified,
        binary resource files, etc.)
      extra_compile_args : [string]
        any extra platform- and compiler-specific information to use
        when compiling the source files in 'sources'.  For platforms and
        compilers where "command line" makes sense, this is typically a
        list of command-line arguments, but for other platforms it could
        be anything.
      extra_link_args : [string]
        any extra platform- and compiler-specific information to use
        when linking object files together to create the extension (or
        to create a new static Python interpreter).  Similar
        interpretation as for 'extra_compile_args'.
      export_symbols : [string]
        list of symbols to be exported from a shared extension.  Not
        used on all platforms, and not generally necessary for Python
        extensions, which typically export exactly one symbol: "init" +
        extension_name.
      swig_opts : [string]
        any extra options to pass to SWIG if a source file has the .i
        extension.
      depends : [string]
        list of files that the extension depends on
      language : string
        extension language (i.e. "c", "c++", "objc"). Will be detected
        from the source extensions if not provided.
      optional : boolean
        specifies that a build failure in the extension should not abort the
        build process, but simply not install the failing extension.
    

<a name="Extension.__init___1296968659"></a>
#### `Extension.__init__(self, name, sources, include_dirs=None, define_macros=None, undef_macros=None, library_dirs=None, libraries=None, runtime_library_dirs=None, extra_objects=None, extra_compile_args=None, extra_link_args=None, export_symbols=None, swig_opts=None, depends=None, language=None, optional=None, **kw)`

None

<a name="Extension.__repr___2023873679"></a>
#### `Extension.__repr__(self)`

None

<a name="distutils.fancy_getopt_310386000"></a>
## distutils.fancy_getopt

<a name="distutils.fancy_getopt.FancyGetopt_730766271"></a>
### distutils.fancy_getopt.FancyGetopt(self, option_table=None)

Wrapper around the standard 'getopt()' module that provides some
    handy extra functionality:
      * short and long options are tied together
      * options have help strings, and help text can be assembled
        from them
      * options set attributes of a passed-in object
      * boolean options can have "negative aliases" -- eg. if
        --quiet is the "negative alias" of --verbose, then "--quiet"
        on the command line sets 'verbose' to false
    

<a name="FancyGetopt.__init___391453862"></a>
#### `FancyGetopt.__init__(self, option_table=None)`

None

<a name="FancyGetopt._build_index_1444118159"></a>
#### `FancyGetopt._build_index(self)`

None

<a name="FancyGetopt._check_alias_dict_118328429"></a>
#### `FancyGetopt._check_alias_dict(self, aliases, what)`

None

<a name="FancyGetopt._grok_option_table_979055245"></a>
#### `FancyGetopt._grok_option_table(self)`

Populate the various data structures that keep tabs on the
        option table.  Called by 'getopt()' before it can do anything
        worthwhile.
        

<a name="FancyGetopt.add_option_995751347"></a>
#### `FancyGetopt.add_option(self, long_option, short_option=None, help_string=None)`

None

<a name="FancyGetopt.generate_help_1026363145"></a>
#### `FancyGetopt.generate_help(self, header=None)`

Generate help text (a list of strings, one per suggested line of
        output) from the option table for this FancyGetopt object.
        

<a name="FancyGetopt.get_attr_name_415219163"></a>
#### `FancyGetopt.get_attr_name(self, long_option)`

Translate long option name 'long_option' to the form it
        has as an attribute of some object: ie., translate hyphens
        to underscores.

<a name="FancyGetopt.get_option_order_514337364"></a>
#### `FancyGetopt.get_option_order(self)`

Returns the list of (option, value) tuples processed by the
        previous run of 'getopt()'.  Raises RuntimeError if
        'getopt()' hasn't been called yet.
        

<a name="FancyGetopt.getopt_294991514"></a>
#### `FancyGetopt.getopt(self, args=None, object=None)`

Parse command-line options in args. Store as attributes on object.

        If 'args' is None or not supplied, uses 'sys.argv[1:]'.  If
        'object' is None or not supplied, creates a new OptionDummy
        object, stores option values there, and returns a tuple (args,
        object).  If 'object' is supplied, it is modified in place and
        'getopt()' just returns 'args'; in both cases, the returned
        'args' is a modified copy of the passed-in 'args' list, which
        is left untouched.
        

<a name="FancyGetopt.has_option_408185363"></a>
#### `FancyGetopt.has_option(self, long_option)`

Return true if the option table for this parser has an
        option with long name 'long_option'.

<a name="FancyGetopt.print_help_1103953632"></a>
#### `FancyGetopt.print_help(self, header=None, file=None)`

None

<a name="FancyGetopt.set_aliases_1810892686"></a>
#### `FancyGetopt.set_aliases(self, alias)`

Set the aliases for this option parser.

<a name="FancyGetopt.set_negative_aliases_749037856"></a>
#### `FancyGetopt.set_negative_aliases(self, negative_alias)`

Set the negative aliases for this option parser.
        'negative_alias' should be a dictionary mapping option names to
        option names, both the key and value must already be defined
        in the option table.

<a name="FancyGetopt.set_option_table_1853321417"></a>
#### `FancyGetopt.set_option_table(self, option_table)`

None

<a name="distutils.fancy_getopt.OptionDummy_22597836"></a>
### distutils.fancy_getopt.OptionDummy(self, options=[])

Dummy class just used as a place to hold command-line option
    values as instance attributes.

<a name="OptionDummy.__init___205744830"></a>
#### `OptionDummy.__init__(self, options=[])`

Create a new OptionDummy instance.  The attributes listed in
        'options' will be initialized to None.

<a name="distutils.file_util_424009387"></a>
## distutils.file_util

<a name="distutils.log_727395436"></a>
## distutils.log

<a name="distutils.log.Log_723538835"></a>
### distutils.log.Log(self, threshold=3)

None

<a name="Log.__init___783981344"></a>
#### `Log.__init__(self, threshold=3)`

None

<a name="Log._log_1895113537"></a>
#### `Log._log(self, level, msg, args)`

None

<a name="Log.debug_154216507"></a>
#### `Log.debug(self, msg, *args)`

None

<a name="Log.error_1223014898"></a>
#### `Log.error(self, msg, *args)`

None

<a name="Log.fatal_1141627102"></a>
#### `Log.fatal(self, msg, *args)`

None

<a name="Log.info_128364290"></a>
#### `Log.info(self, msg, *args)`

None

<a name="Log.log_1397817601"></a>
#### `Log.log(self, level, msg, *args)`

None

<a name="Log.warn_625023016"></a>
#### `Log.warn(self, msg, *args)`

None

<a name="_virtualenv_distutils_1884558016"></a>
## _virtualenv_distutils

<a name="distutils.spawn_381508274"></a>
## distutils.spawn

<a name="distutils.sysconfig_1670193064"></a>
## distutils.sysconfig

<a name="distutils.util_407928641"></a>
## distutils.util

<a name="distutils.util.Mixin2to3_551833640"></a>
### distutils.util.Mixin2to3(self, /, *args, **kwargs)

Mixin class for commands that run 2to3.
    To configure 2to3, setup scripts may either change
    the class variables, or inherit from individual commands
    to override how 2to3 is invoked.

<a name="Mixin2to3.run_2to3_1226325292"></a>
#### `Mixin2to3.run_2to3(self, files)`

None

