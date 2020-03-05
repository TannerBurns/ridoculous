- [ distutils.cmd ](#distutils.cmd_1367970031)
	- [ distutils.cmd.Command ](#distutils.cmd.Command_1826269518)
		- [ Command.__getattr__ ](#Command.__getattr___1684982512)
		- [ Command.__init__ ](#Command.__init___607161029)
		- [ Command._ensure_stringlike ](#Command._ensure_stringlike_310695404)
		- [ Command._ensure_tested_string ](#Command._ensure_tested_string_474654751)
		- [ Command.announce ](#Command.announce_514580352)
		- [ Command.copy_file ](#Command.copy_file_160735974)
		- [ Command.copy_tree ](#Command.copy_tree_1328979272)
		- [ Command.debug_print ](#Command.debug_print_283847946)
		- [ Command.dump_options ](#Command.dump_options_1133285078)
		- [ Command.ensure_dirname ](#Command.ensure_dirname_201023732)
		- [ Command.ensure_filename ](#Command.ensure_filename_47057984)
		- [ Command.ensure_finalized ](#Command.ensure_finalized_643130783)
		- [ Command.ensure_string ](#Command.ensure_string_1709379107)
		- [ Command.ensure_string_list ](#Command.ensure_string_list_414134839)
		- [ Command.execute ](#Command.execute_1729662775)
		- [ Command.finalize_options ](#Command.finalize_options_158778118)
		- [ Command.get_command_name ](#Command.get_command_name_923473241)
		- [ Command.get_finalized_command ](#Command.get_finalized_command_1665652895)
		- [ Command.get_sub_commands ](#Command.get_sub_commands_1299476987)
		- [ Command.initialize_options ](#Command.initialize_options_753972443)
		- [ Command.make_archive ](#Command.make_archive_1106153658)
		- [ Command.make_file ](#Command.make_file_1064135465)
		- [ Command.mkpath ](#Command.mkpath_1033456758)
		- [ Command.move_file ](#Command.move_file_98697897)
		- [ Command.reinitialize_command ](#Command.reinitialize_command_895217986)
		- [ Command.run ](#Command.run_1857787309)
		- [ Command.run_command ](#Command.run_command_1504674045)
		- [ Command.set_undefined_options ](#Command.set_undefined_options_162040537)
		- [ Command.spawn ](#Command.spawn_1531602270)
		- [ Command.warn ](#Command.warn_1076232486)
- [ distutils.config ](#distutils.config_376132367)
	- [ distutils.config.PyPIRCCommand ](#distutils.config.PyPIRCCommand_888227476)
		- [ PyPIRCCommand._get_rc_file ](#PyPIRCCommand._get_rc_file_1246683162)
		- [ PyPIRCCommand._read_pypi_response ](#PyPIRCCommand._read_pypi_response_1946784252)
		- [ PyPIRCCommand._read_pypirc ](#PyPIRCCommand._read_pypirc_1428569189)
		- [ PyPIRCCommand._store_pypirc ](#PyPIRCCommand._store_pypirc_1759598218)
		- [ PyPIRCCommand.finalize_options ](#PyPIRCCommand.finalize_options_869770026)
		- [ PyPIRCCommand.initialize_options ](#PyPIRCCommand.initialize_options_534611092)
- [ distutils.dist ](#distutils.dist_1871677696)
	- [ distutils.dist.Distribution ](#distutils.dist.Distribution_1800475928)
		- [ Distribution.__init__ ](#Distribution.__init___1853504354)
		- [ Distribution._get_toplevel_options ](#Distribution._get_toplevel_options_610056902)
		- [ Distribution._parse_command_opts ](#Distribution._parse_command_opts_195566791)
		- [ Distribution._set_command_options ](#Distribution._set_command_options_878680655)
		- [ Distribution._show_help ](#Distribution._show_help_671683127)
		- [ Distribution.announce ](#Distribution.announce_433335322)
		- [ Distribution.dump_option_dicts ](#Distribution.dump_option_dicts_691785792)
		- [ Distribution.finalize_options ](#Distribution.finalize_options_1935517183)
		- [ Distribution.get_command_class ](#Distribution.get_command_class_1912933820)
		- [ Distribution.get_command_list ](#Distribution.get_command_list_1273615621)
		- [ Distribution.get_command_obj ](#Distribution.get_command_obj_1033437308)
		- [ Distribution.get_command_packages ](#Distribution.get_command_packages_610557699)
		- [ Distribution.get_option_dict ](#Distribution.get_option_dict_1338172695)
		- [ Distribution.handle_display_options ](#Distribution.handle_display_options_1214864355)
		- [ Distribution.has_c_libraries ](#Distribution.has_c_libraries_686701765)
		- [ Distribution.has_data_files ](#Distribution.has_data_files_2090233743)
		- [ Distribution.has_ext_modules ](#Distribution.has_ext_modules_1786966524)
		- [ Distribution.has_headers ](#Distribution.has_headers_2140796816)
		- [ Distribution.has_modules ](#Distribution.has_modules_440551571)
		- [ Distribution.has_pure_modules ](#Distribution.has_pure_modules_657239041)
		- [ Distribution.has_scripts ](#Distribution.has_scripts_207151625)
		- [ Distribution.is_pure ](#Distribution.is_pure_255073769)
		- [ Distribution.parse_command_line ](#Distribution.parse_command_line_1259349788)
		- [ Distribution.parse_config_files ](#Distribution.parse_config_files_644804565)
		- [ Distribution.print_command_list ](#Distribution.print_command_list_55534003)
		- [ Distribution.print_commands ](#Distribution.print_commands_875402934)
		- [ Distribution.reinitialize_command ](#Distribution.reinitialize_command_1534159254)
		- [ Distribution.run_command ](#Distribution.run_command_1490741969)
		- [ Distribution.run_commands ](#Distribution.run_commands_1168776298)
	- [ distutils.dist.DistributionMetadata ](#distutils.dist.DistributionMetadata_1765298581)
		- [ DistributionMetadata.__init__ ](#DistributionMetadata.__init___511627922)
		- [ DistributionMetadata._write_list ](#DistributionMetadata._write_list_1180458245)
		- [ DistributionMetadata.get_author ](#DistributionMetadata.get_author_77594966)
		- [ DistributionMetadata.get_author_email ](#DistributionMetadata.get_author_email_32919814)
		- [ DistributionMetadata.get_classifiers ](#DistributionMetadata.get_classifiers_1169790099)
		- [ DistributionMetadata.get_contact ](#DistributionMetadata.get_contact_2039982457)
		- [ DistributionMetadata.get_contact_email ](#DistributionMetadata.get_contact_email_1490537017)
		- [ DistributionMetadata.get_description ](#DistributionMetadata.get_description_1946262946)
		- [ DistributionMetadata.get_download_url ](#DistributionMetadata.get_download_url_537567615)
		- [ DistributionMetadata.get_fullname ](#DistributionMetadata.get_fullname_2064848557)
		- [ DistributionMetadata.get_keywords ](#DistributionMetadata.get_keywords_50447118)
		- [ DistributionMetadata.get_license ](#DistributionMetadata.get_license_1923363342)
		- [ DistributionMetadata.get_license ](#DistributionMetadata.get_license_1923363342)
		- [ DistributionMetadata.get_long_description ](#DistributionMetadata.get_long_description_1340362464)
		- [ DistributionMetadata.get_maintainer ](#DistributionMetadata.get_maintainer_1106525876)
		- [ DistributionMetadata.get_maintainer_email ](#DistributionMetadata.get_maintainer_email_336215624)
		- [ DistributionMetadata.get_name ](#DistributionMetadata.get_name_193823249)
		- [ DistributionMetadata.get_obsoletes ](#DistributionMetadata.get_obsoletes_698577059)
		- [ DistributionMetadata.get_platforms ](#DistributionMetadata.get_platforms_1464408328)
		- [ DistributionMetadata.get_provides ](#DistributionMetadata.get_provides_1149218251)
		- [ DistributionMetadata.get_requires ](#DistributionMetadata.get_requires_1473251117)
		- [ DistributionMetadata.get_url ](#DistributionMetadata.get_url_451680316)
		- [ DistributionMetadata.get_version ](#DistributionMetadata.get_version_1150369583)
		- [ DistributionMetadata.read_pkg_file ](#DistributionMetadata.read_pkg_file_1216118664)
		- [ DistributionMetadata.set_classifiers ](#DistributionMetadata.set_classifiers_856219950)
		- [ DistributionMetadata.set_keywords ](#DistributionMetadata.set_keywords_1738917351)
		- [ DistributionMetadata.set_obsoletes ](#DistributionMetadata.set_obsoletes_699785093)
		- [ DistributionMetadata.set_platforms ](#DistributionMetadata.set_platforms_1546786450)
		- [ DistributionMetadata.set_provides ](#DistributionMetadata.set_provides_451616874)
		- [ DistributionMetadata.set_requires ](#DistributionMetadata.set_requires_1439477911)
		- [ DistributionMetadata.write_pkg_file ](#DistributionMetadata.write_pkg_file_1243044579)
		- [ DistributionMetadata.write_pkg_info ](#DistributionMetadata.write_pkg_info_1499607057)
- [ distutils.errors ](#distutils.errors_615758800)
	- [ distutils.errors.CCompilerError ](#distutils.errors.CCompilerError_489562513)
	- [ distutils.errors.CompileError ](#distutils.errors.CompileError_2118020224)
	- [ distutils.errors.DistutilsArgError ](#distutils.errors.DistutilsArgError_1257368548)
	- [ distutils.errors.DistutilsByteCompileError ](#distutils.errors.DistutilsByteCompileError_1795026548)
	- [ distutils.errors.DistutilsClassError ](#distutils.errors.DistutilsClassError_102650573)
	- [ distutils.errors.DistutilsError ](#distutils.errors.DistutilsError_1016881250)
	- [ distutils.errors.DistutilsExecError ](#distutils.errors.DistutilsExecError_1971907463)
	- [ distutils.errors.DistutilsFileError ](#distutils.errors.DistutilsFileError_1845814768)
	- [ distutils.errors.DistutilsGetoptError ](#distutils.errors.DistutilsGetoptError_563620136)
	- [ distutils.errors.DistutilsInternalError ](#distutils.errors.DistutilsInternalError_2029758928)
	- [ distutils.errors.DistutilsModuleError ](#distutils.errors.DistutilsModuleError_1894677276)
	- [ distutils.errors.DistutilsOptionError ](#distutils.errors.DistutilsOptionError_328283483)
	- [ distutils.errors.DistutilsPlatformError ](#distutils.errors.DistutilsPlatformError_1091057729)
	- [ distutils.errors.DistutilsSetupError ](#distutils.errors.DistutilsSetupError_790730189)
	- [ distutils.errors.DistutilsTemplateError ](#distutils.errors.DistutilsTemplateError_98426290)
	- [ distutils.errors.LibError ](#distutils.errors.LibError_921096887)
	- [ distutils.errors.LinkError ](#distutils.errors.LinkError_2131984186)
	- [ distutils.errors.PreprocessError ](#distutils.errors.PreprocessError_639855432)
	- [ distutils.errors.UnknownFileError ](#distutils.errors.UnknownFileError_1973101983)
- [ distutils.extension ](#distutils.extension_52505578)
	- [ distutils.extension.Extension ](#distutils.extension.Extension_1251788304)
		- [ Extension.__init__ ](#Extension.__init___1301196714)
		- [ Extension.__repr__ ](#Extension.__repr___1720337318)
- [ distutils.fancy_getopt ](#distutils.fancy_getopt_1539860445)
	- [ distutils.fancy_getopt.FancyGetopt ](#distutils.fancy_getopt.FancyGetopt_1369507288)
		- [ FancyGetopt.__init__ ](#FancyGetopt.__init___1000404788)
		- [ FancyGetopt._build_index ](#FancyGetopt._build_index_309200474)
		- [ FancyGetopt._check_alias_dict ](#FancyGetopt._check_alias_dict_1408086727)
		- [ FancyGetopt._grok_option_table ](#FancyGetopt._grok_option_table_2039400878)
		- [ FancyGetopt.add_option ](#FancyGetopt.add_option_1002664853)
		- [ FancyGetopt.generate_help ](#FancyGetopt.generate_help_1828901599)
		- [ FancyGetopt.get_attr_name ](#FancyGetopt.get_attr_name_492310190)
		- [ FancyGetopt.get_option_order ](#FancyGetopt.get_option_order_504866980)
		- [ FancyGetopt.getopt ](#FancyGetopt.getopt_726500129)
		- [ FancyGetopt.has_option ](#FancyGetopt.has_option_1084693968)
		- [ FancyGetopt.print_help ](#FancyGetopt.print_help_152685416)
		- [ FancyGetopt.set_aliases ](#FancyGetopt.set_aliases_1841219157)
		- [ FancyGetopt.set_negative_aliases ](#FancyGetopt.set_negative_aliases_1579428126)
		- [ FancyGetopt.set_option_table ](#FancyGetopt.set_option_table_1638126737)
	- [ distutils.fancy_getopt.OptionDummy ](#distutils.fancy_getopt.OptionDummy_1103708956)
		- [ OptionDummy.__init__ ](#OptionDummy.__init___663412451)
- [ distutils.log ](#distutils.log_880671927)
	- [ distutils.log.Log ](#distutils.log.Log_1791316898)
		- [ Log.__init__ ](#Log.__init___96795857)
		- [ Log._log ](#Log._log_853726519)
		- [ Log.debug ](#Log.debug_153411802)
		- [ Log.error ](#Log.error_1972683729)
		- [ Log.fatal ](#Log.fatal_1545660352)
		- [ Log.info ](#Log.info_462281130)
		- [ Log.log ](#Log.log_548674238)
		- [ Log.warn ](#Log.warn_252498183)
- [ distutils.util ](#distutils.util_1394263673)
	- [ distutils.util.Mixin2to3 ](#distutils.util.Mixin2to3_599796225)
		- [ Mixin2to3.run_2to3 ](#Mixin2to3.run_2to3_1700750410)


<a name="distutils.cmd_1367970031"></a>
## distutils.cmd

<a name="distutils.cmd.Command_1826269518"></a>
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
    

<a name="Command.__getattr___1684982512"></a>
#### `Command.__getattr__(self, attr)`

None

<a name="Command.__init___607161029"></a>
#### `Command.__init__(self, dist)`

Create and initialize a new Command object.  Most importantly,
        invokes the 'initialize_options()' method, which is the real
        initializer and depends on the actual command being
        instantiated.
        

<a name="Command._ensure_stringlike_310695404"></a>
#### `Command._ensure_stringlike(self, option, what, default=None)`

None

<a name="Command._ensure_tested_string_474654751"></a>
#### `Command._ensure_tested_string(self, option, tester, what, error_fmt, default=None)`

None

<a name="Command.announce_514580352"></a>
#### `Command.announce(self, msg, level=1)`

If the current verbosity level is of greater than or equal to
        'level' print 'msg' to stdout.
        

<a name="Command.copy_file_160735974"></a>
#### `Command.copy_file(self, infile, outfile, preserve_mode=1, preserve_times=1, link=None, level=1)`

Copy a file respecting verbose, dry-run and force flags.  (The
        former two default to whatever is in the Distribution object, and
        the latter defaults to false for commands that don't define it.)

<a name="Command.copy_tree_1328979272"></a>
#### `Command.copy_tree(self, infile, outfile, preserve_mode=1, preserve_times=1, preserve_symlinks=0, level=1)`

Copy an entire directory tree respecting verbose, dry-run,
        and force flags.
        

<a name="Command.debug_print_283847946"></a>
#### `Command.debug_print(self, msg)`

Print 'msg' to stdout if the global DEBUG (taken from the
        DISTUTILS_DEBUG environment variable) flag is true.
        

<a name="Command.dump_options_1133285078"></a>
#### `Command.dump_options(self, header=None, indent='')`

None

<a name="Command.ensure_dirname_201023732"></a>
#### `Command.ensure_dirname(self, option)`

None

<a name="Command.ensure_filename_47057984"></a>
#### `Command.ensure_filename(self, option)`

Ensure that 'option' is the name of an existing file.

<a name="Command.ensure_finalized_643130783"></a>
#### `Command.ensure_finalized(self)`

None

<a name="Command.ensure_string_1709379107"></a>
#### `Command.ensure_string(self, option, default=None)`

Ensure that 'option' is a string; if not defined, set it to
        'default'.
        

<a name="Command.ensure_string_list_414134839"></a>
#### `Command.ensure_string_list(self, option)`

Ensure that 'option' is a list of strings.  If 'option' is
        currently a string, we split it either on /,\s*/ or /\s+/, so
        "foo bar baz", "foo,bar,baz", and "foo,   bar baz" all become
        ["foo", "bar", "baz"].
        

<a name="Command.execute_1729662775"></a>
#### `Command.execute(self, func, args, msg=None, level=1)`

None

<a name="Command.finalize_options_158778118"></a>
#### `Command.finalize_options(self)`

Set final values for all the options that this command supports.
        This is always called as late as possible, ie.  after any option
        assignments from the command-line or from other commands have been
        done.  Thus, this is the place to code option dependencies: if
        'foo' depends on 'bar', then it is safe to set 'foo' from 'bar' as
        long as 'foo' still has the same value it was assigned in
        'initialize_options()'.

        This method must be implemented by all command classes.
        

<a name="Command.get_command_name_923473241"></a>
#### `Command.get_command_name(self)`

None

<a name="Command.get_finalized_command_1665652895"></a>
#### `Command.get_finalized_command(self, command, create=1)`

Wrapper around Distribution's 'get_command_obj()' method: find
        (create if necessary and 'create' is true) the command object for
        'command', call its 'ensure_finalized()' method, and return the
        finalized command object.
        

<a name="Command.get_sub_commands_1299476987"></a>
#### `Command.get_sub_commands(self)`

Determine the sub-commands that are relevant in the current
        distribution (ie., that need to be run).  This is based on the
        'sub_commands' class attribute: each tuple in that list may include
        a method that we call to determine if the subcommand needs to be
        run for the current distribution.  Return a list of command names.
        

<a name="Command.initialize_options_753972443"></a>
#### `Command.initialize_options(self)`

Set default values for all the options that this command
        supports.  Note that these defaults may be overridden by other
        commands, by the setup script, by config files, or by the
        command-line.  Thus, this is not the place to code dependencies
        between options; generally, 'initialize_options()' implementations
        are just a bunch of "self.foo = None" assignments.

        This method must be implemented by all command classes.
        

<a name="Command.make_archive_1106153658"></a>
#### `Command.make_archive(self, base_name, format, root_dir=None, base_dir=None, owner=None, group=None)`

None

<a name="Command.make_file_1064135465"></a>
#### `Command.make_file(self, infiles, outfile, func, args, exec_msg=None, skip_msg=None, level=1)`

Special case of 'execute()' for operations that process one or
        more input files and generate one output file.  Works just like
        'execute()', except the operation is skipped and a different
        message printed if 'outfile' already exists and is newer than all
        files listed in 'infiles'.  If the command defined 'self.force',
        and it is true, then the command is unconditionally run -- does no
        timestamp checks.
        

<a name="Command.mkpath_1033456758"></a>
#### `Command.mkpath(self, name, mode=511)`

None

<a name="Command.move_file_98697897"></a>
#### `Command.move_file(self, src, dst, level=1)`

Move a file respecting dry-run flag.

<a name="Command.reinitialize_command_895217986"></a>
#### `Command.reinitialize_command(self, command, reinit_subcommands=0)`

None

<a name="Command.run_1857787309"></a>
#### `Command.run(self)`

A command's raison d'etre: carry out the action it exists to
        perform, controlled by the options initialized in
        'initialize_options()', customized by other commands, the setup
        script, the command-line, and config files, and finalized in
        'finalize_options()'.  All terminal output and filesystem
        interaction should be done by 'run()'.

        This method must be implemented by all command classes.
        

<a name="Command.run_command_1504674045"></a>
#### `Command.run_command(self, command)`

Run some other command: uses the 'run_command()' method of
        Distribution, which creates and finalizes the command object if
        necessary and then invokes its 'run()' method.
        

<a name="Command.set_undefined_options_162040537"></a>
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
        

<a name="Command.spawn_1531602270"></a>
#### `Command.spawn(self, cmd, search_path=1, level=1)`

Spawn an external command respecting dry-run flag.

<a name="Command.warn_1076232486"></a>
#### `Command.warn(self, msg)`

None

<a name="distutils.config_376132367"></a>
## distutils.config

<a name="distutils.config.PyPIRCCommand_888227476"></a>
### distutils.config.PyPIRCCommand(self, dist)

Base command that knows how to handle the .pypirc file
    

<a name="PyPIRCCommand._get_rc_file_1246683162"></a>
#### `PyPIRCCommand._get_rc_file(self)`

Returns rc file path.

<a name="PyPIRCCommand._read_pypi_response_1946784252"></a>
#### `PyPIRCCommand._read_pypi_response(self, response)`

Read and decode a PyPI HTTP response.

<a name="PyPIRCCommand._read_pypirc_1428569189"></a>
#### `PyPIRCCommand._read_pypirc(self)`

Reads the .pypirc file.

<a name="PyPIRCCommand._store_pypirc_1759598218"></a>
#### `PyPIRCCommand._store_pypirc(self, username, password)`

Creates a default .pypirc file.

<a name="PyPIRCCommand.finalize_options_869770026"></a>
#### `PyPIRCCommand.finalize_options(self)`

Finalizes options.

<a name="PyPIRCCommand.initialize_options_534611092"></a>
#### `PyPIRCCommand.initialize_options(self)`

Initialize options.

<a name="distutils.dist_1871677696"></a>
## distutils.dist

<a name="distutils.dist.Distribution_1800475928"></a>
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
    

<a name="Distribution.__init___1853504354"></a>
#### `Distribution.__init__(self, attrs=None)`

Construct a new Distribution instance: initialize all the
        attributes of a Distribution, and then use 'attrs' (a dictionary
        mapping attribute names to values) to assign some of those
        attributes their "real" values.  (Any attributes not mentioned in
        'attrs' will be assigned to some null value: 0, None, an empty list
        or dictionary, etc.)  Most importantly, initialize the
        'command_obj' attribute to the empty dictionary; this will be
        filled in with real command objects by 'parse_command_line()'.
        

<a name="Distribution._get_toplevel_options_610056902"></a>
#### `Distribution._get_toplevel_options(self)`

Return the non-display options recognized at the top level.

        This includes options that are recognized *only* at the top
        level as well as options recognized for commands.
        

<a name="Distribution._parse_command_opts_195566791"></a>
#### `Distribution._parse_command_opts(self, parser, args)`

Parse the command-line options for a single command.
        'parser' must be a FancyGetopt instance; 'args' must be the list
        of arguments, starting with the current command (whose options
        we are about to parse).  Returns a new version of 'args' with
        the next command at the front of the list; will be the empty
        list if there are no more commands on the command line.  Returns
        None if the user asked for help on this command.
        

<a name="Distribution._set_command_options_878680655"></a>
#### `Distribution._set_command_options(self, command_obj, option_dict=None)`

Set the options for 'command_obj' from 'option_dict'.  Basically
        this means copying elements of a dictionary ('option_dict') to
        attributes of an instance ('command').

        'command_obj' must be a Command instance.  If 'option_dict' is not
        supplied, uses the standard option dictionary for this command
        (from 'self.command_options').
        

<a name="Distribution._show_help_671683127"></a>
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
        

<a name="Distribution.announce_433335322"></a>
#### `Distribution.announce(self, msg, level=2)`

None

<a name="Distribution.dump_option_dicts_691785792"></a>
#### `Distribution.dump_option_dicts(self, header=None, commands=None, indent='')`

None

<a name="Distribution.finalize_options_1935517183"></a>
#### `Distribution.finalize_options(self)`

Set final values for all the options on the Distribution
        instance, analogous to the .finalize_options() method of Command
        objects.
        

<a name="Distribution.get_command_class_1912933820"></a>
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
        

<a name="Distribution.get_command_list_1273615621"></a>
#### `Distribution.get_command_list(self)`

Get a list of (command, description) tuples.
        The list is divided into "standard commands" (listed in
        distutils.command.__all__) and "extra commands" (mentioned in
        self.cmdclass, but not a standard command).  The descriptions come
        from the command class attribute 'description'.
        

<a name="Distribution.get_command_obj_1033437308"></a>
#### `Distribution.get_command_obj(self, command, create=1)`

Return the command object for 'command'.  Normally this object
        is cached on a previous call to 'get_command_obj()'; if no command
        object for 'command' is in the cache, then we either create and
        return it (if 'create' is true) or return None.
        

<a name="Distribution.get_command_packages_610557699"></a>
#### `Distribution.get_command_packages(self)`

Return a list of packages from which commands are loaded.

<a name="Distribution.get_option_dict_1338172695"></a>
#### `Distribution.get_option_dict(self, command)`

Get the option dictionary for a given command.  If that
        command's option dictionary hasn't been created yet, then create it
        and return the new dictionary; otherwise, return the existing
        option dictionary.
        

<a name="Distribution.handle_display_options_1214864355"></a>
#### `Distribution.handle_display_options(self, option_order)`

If there were any non-global "display-only" options
        (--help-commands or the metadata display options) on the command
        line, display the requested info and return true; else return
        false.
        

<a name="Distribution.has_c_libraries_686701765"></a>
#### `Distribution.has_c_libraries(self)`

None

<a name="Distribution.has_data_files_2090233743"></a>
#### `Distribution.has_data_files(self)`

None

<a name="Distribution.has_ext_modules_1786966524"></a>
#### `Distribution.has_ext_modules(self)`

None

<a name="Distribution.has_headers_2140796816"></a>
#### `Distribution.has_headers(self)`

None

<a name="Distribution.has_modules_440551571"></a>
#### `Distribution.has_modules(self)`

None

<a name="Distribution.has_pure_modules_657239041"></a>
#### `Distribution.has_pure_modules(self)`

None

<a name="Distribution.has_scripts_207151625"></a>
#### `Distribution.has_scripts(self)`

None

<a name="Distribution.is_pure_255073769"></a>
#### `Distribution.is_pure(self)`

None

<a name="Distribution.parse_command_line_1259349788"></a>
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
        

<a name="Distribution.parse_config_files_644804565"></a>
#### `Distribution.parse_config_files(self, filenames=None)`

None

<a name="Distribution.print_command_list_55534003"></a>
#### `Distribution.print_command_list(self, commands, header, max_length)`

Print a subset of the list of all commands -- used by
        'print_commands()'.
        

<a name="Distribution.print_commands_875402934"></a>
#### `Distribution.print_commands(self)`

Print out a help message listing all available commands with a
        description of each.  The list is divided into "standard commands"
        (listed in distutils.command.__all__) and "extra commands"
        (mentioned in self.cmdclass, but not a standard command).  The
        descriptions come from the command class attribute
        'description'.
        

<a name="Distribution.reinitialize_command_1534159254"></a>
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
        

<a name="Distribution.run_command_1490741969"></a>
#### `Distribution.run_command(self, command)`

Do whatever it takes to run a command (including nothing at all,
        if the command has already been run).  Specifically: if we have
        already created and run the command named by 'command', return
        silently without doing anything.  If the command named by 'command'
        doesn't even have a command object yet, create one.  Then invoke
        'run()' on that command object (or an existing one).
        

<a name="Distribution.run_commands_1168776298"></a>
#### `Distribution.run_commands(self)`

Run each command that was seen on the setup script command line.
        Uses the list of commands found and cache of command objects
        created by 'get_command_obj()'.
        

<a name="distutils.dist.DistributionMetadata_1765298581"></a>
### distutils.dist.DistributionMetadata(self, path=None)

Dummy class to hold the distribution meta-data: name, version,
    author, and so forth.
    

<a name="DistributionMetadata.__init___511627922"></a>
#### `DistributionMetadata.__init__(self, path=None)`

None

<a name="DistributionMetadata._write_list_1180458245"></a>
#### `DistributionMetadata._write_list(self, file, name, values)`

None

<a name="DistributionMetadata.get_author_77594966"></a>
#### `DistributionMetadata.get_author(self)`

None

<a name="DistributionMetadata.get_author_email_32919814"></a>
#### `DistributionMetadata.get_author_email(self)`

None

<a name="DistributionMetadata.get_classifiers_1169790099"></a>
#### `DistributionMetadata.get_classifiers(self)`

None

<a name="DistributionMetadata.get_contact_2039982457"></a>
#### `DistributionMetadata.get_contact(self)`

None

<a name="DistributionMetadata.get_contact_email_1490537017"></a>
#### `DistributionMetadata.get_contact_email(self)`

None

<a name="DistributionMetadata.get_description_1946262946"></a>
#### `DistributionMetadata.get_description(self)`

None

<a name="DistributionMetadata.get_download_url_537567615"></a>
#### `DistributionMetadata.get_download_url(self)`

None

<a name="DistributionMetadata.get_fullname_2064848557"></a>
#### `DistributionMetadata.get_fullname(self)`

None

<a name="DistributionMetadata.get_keywords_50447118"></a>
#### `DistributionMetadata.get_keywords(self)`

None

<a name="DistributionMetadata.get_license_1923363342"></a>
#### `DistributionMetadata.get_license(self)`

None

<a name="DistributionMetadata.get_license_1923363342"></a>
#### `DistributionMetadata.get_license(self)`

None

<a name="DistributionMetadata.get_long_description_1340362464"></a>
#### `DistributionMetadata.get_long_description(self)`

None

<a name="DistributionMetadata.get_maintainer_1106525876"></a>
#### `DistributionMetadata.get_maintainer(self)`

None

<a name="DistributionMetadata.get_maintainer_email_336215624"></a>
#### `DistributionMetadata.get_maintainer_email(self)`

None

<a name="DistributionMetadata.get_name_193823249"></a>
#### `DistributionMetadata.get_name(self)`

None

<a name="DistributionMetadata.get_obsoletes_698577059"></a>
#### `DistributionMetadata.get_obsoletes(self)`

None

<a name="DistributionMetadata.get_platforms_1464408328"></a>
#### `DistributionMetadata.get_platforms(self)`

None

<a name="DistributionMetadata.get_provides_1149218251"></a>
#### `DistributionMetadata.get_provides(self)`

None

<a name="DistributionMetadata.get_requires_1473251117"></a>
#### `DistributionMetadata.get_requires(self)`

None

<a name="DistributionMetadata.get_url_451680316"></a>
#### `DistributionMetadata.get_url(self)`

None

<a name="DistributionMetadata.get_version_1150369583"></a>
#### `DistributionMetadata.get_version(self)`

None

<a name="DistributionMetadata.read_pkg_file_1216118664"></a>
#### `DistributionMetadata.read_pkg_file(self, file)`

Reads the metadata values from a file object.

<a name="DistributionMetadata.set_classifiers_856219950"></a>
#### `DistributionMetadata.set_classifiers(self, value)`

None

<a name="DistributionMetadata.set_keywords_1738917351"></a>
#### `DistributionMetadata.set_keywords(self, value)`

None

<a name="DistributionMetadata.set_obsoletes_699785093"></a>
#### `DistributionMetadata.set_obsoletes(self, value)`

None

<a name="DistributionMetadata.set_platforms_1546786450"></a>
#### `DistributionMetadata.set_platforms(self, value)`

None

<a name="DistributionMetadata.set_provides_451616874"></a>
#### `DistributionMetadata.set_provides(self, value)`

None

<a name="DistributionMetadata.set_requires_1439477911"></a>
#### `DistributionMetadata.set_requires(self, value)`

None

<a name="DistributionMetadata.write_pkg_file_1243044579"></a>
#### `DistributionMetadata.write_pkg_file(self, file)`

Write the PKG-INFO format data to a file object.
        

<a name="DistributionMetadata.write_pkg_info_1499607057"></a>
#### `DistributionMetadata.write_pkg_info(self, base_dir)`

Write the PKG-INFO file into the release tree.
        

<a name="distutils.errors_615758800"></a>
## distutils.errors

<a name="distutils.errors.CCompilerError_489562513"></a>
### distutils.errors.CCompilerError(self, /, *args, **kwargs)

Some compile/link operation failed.

<a name="distutils.errors.CompileError_2118020224"></a>
### distutils.errors.CompileError(self, /, *args, **kwargs)

Failure to compile one or more C/C++ source files.

<a name="distutils.errors.DistutilsArgError_1257368548"></a>
### distutils.errors.DistutilsArgError(self, /, *args, **kwargs)

Raised by fancy_getopt in response to getopt.error -- ie. an
    error in the command line usage.

<a name="distutils.errors.DistutilsByteCompileError_1795026548"></a>
### distutils.errors.DistutilsByteCompileError(self, /, *args, **kwargs)

Byte compile error.

<a name="distutils.errors.DistutilsClassError_102650573"></a>
### distutils.errors.DistutilsClassError(self, /, *args, **kwargs)

Some command class (or possibly distribution class, if anyone
    feels a need to subclass Distribution) is found not to be holding
    up its end of the bargain, ie. implementing some part of the
    "command "interface.

<a name="distutils.errors.DistutilsError_1016881250"></a>
### distutils.errors.DistutilsError(self, /, *args, **kwargs)

The root of all Distutils evil.

<a name="distutils.errors.DistutilsExecError_1971907463"></a>
### distutils.errors.DistutilsExecError(self, /, *args, **kwargs)

Any problems executing an external program (such as the C
    compiler, when compiling C files).

<a name="distutils.errors.DistutilsFileError_1845814768"></a>
### distutils.errors.DistutilsFileError(self, /, *args, **kwargs)

Any problems in the filesystem: expected file not found, etc.
    Typically this is for problems that we detect before OSError
    could be raised.

<a name="distutils.errors.DistutilsGetoptError_563620136"></a>
### distutils.errors.DistutilsGetoptError(self, /, *args, **kwargs)

The option table provided to 'fancy_getopt()' is bogus.

<a name="distutils.errors.DistutilsInternalError_2029758928"></a>
### distutils.errors.DistutilsInternalError(self, /, *args, **kwargs)

Internal inconsistencies or impossibilities (obviously, this
    should never be seen if the code is working!).

<a name="distutils.errors.DistutilsModuleError_1894677276"></a>
### distutils.errors.DistutilsModuleError(self, /, *args, **kwargs)

Unable to load an expected module, or to find an expected class
    within some module (in particular, command modules and classes).

<a name="distutils.errors.DistutilsOptionError_328283483"></a>
### distutils.errors.DistutilsOptionError(self, /, *args, **kwargs)

Syntactic/semantic errors in command options, such as use of
    mutually conflicting options, or inconsistent options,
    badly-spelled values, etc.  No distinction is made between option
    values originating in the setup script, the command line, config
    files, or what-have-you -- but if we *know* something originated in
    the setup script, we'll raise DistutilsSetupError instead.

<a name="distutils.errors.DistutilsPlatformError_1091057729"></a>
### distutils.errors.DistutilsPlatformError(self, /, *args, **kwargs)

We don't know how to do something on the current platform (but
    we do know how to do it on some platform) -- eg. trying to compile
    C files on a platform not supported by a CCompiler subclass.

<a name="distutils.errors.DistutilsSetupError_790730189"></a>
### distutils.errors.DistutilsSetupError(self, /, *args, **kwargs)

For errors that can be definitely blamed on the setup script,
    such as invalid keyword arguments to 'setup()'.

<a name="distutils.errors.DistutilsTemplateError_98426290"></a>
### distutils.errors.DistutilsTemplateError(self, /, *args, **kwargs)

Syntax error in a file list template.

<a name="distutils.errors.LibError_921096887"></a>
### distutils.errors.LibError(self, /, *args, **kwargs)

Failure to create a static library from one or more C/C++ object
    files.

<a name="distutils.errors.LinkError_2131984186"></a>
### distutils.errors.LinkError(self, /, *args, **kwargs)

Failure to link one or more C/C++ object files into an executable
    or shared library file.

<a name="distutils.errors.PreprocessError_639855432"></a>
### distutils.errors.PreprocessError(self, /, *args, **kwargs)

Failure to preprocess one or more C/C++ files.

<a name="distutils.errors.UnknownFileError_1973101983"></a>
### distutils.errors.UnknownFileError(self, /, *args, **kwargs)

Attempt to process an unknown file type.

<a name="distutils.extension_52505578"></a>
## distutils.extension

<a name="distutils.extension.Extension_1251788304"></a>
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
    

<a name="Extension.__init___1301196714"></a>
#### `Extension.__init__(self, name, sources, include_dirs=None, define_macros=None, undef_macros=None, library_dirs=None, libraries=None, runtime_library_dirs=None, extra_objects=None, extra_compile_args=None, extra_link_args=None, export_symbols=None, swig_opts=None, depends=None, language=None, optional=None, **kw)`

None

<a name="Extension.__repr___1720337318"></a>
#### `Extension.__repr__(self)`

None

<a name="distutils.fancy_getopt_1539860445"></a>
## distutils.fancy_getopt

<a name="distutils.fancy_getopt.FancyGetopt_1369507288"></a>
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
    

<a name="FancyGetopt.__init___1000404788"></a>
#### `FancyGetopt.__init__(self, option_table=None)`

None

<a name="FancyGetopt._build_index_309200474"></a>
#### `FancyGetopt._build_index(self)`

None

<a name="FancyGetopt._check_alias_dict_1408086727"></a>
#### `FancyGetopt._check_alias_dict(self, aliases, what)`

None

<a name="FancyGetopt._grok_option_table_2039400878"></a>
#### `FancyGetopt._grok_option_table(self)`

Populate the various data structures that keep tabs on the
        option table.  Called by 'getopt()' before it can do anything
        worthwhile.
        

<a name="FancyGetopt.add_option_1002664853"></a>
#### `FancyGetopt.add_option(self, long_option, short_option=None, help_string=None)`

None

<a name="FancyGetopt.generate_help_1828901599"></a>
#### `FancyGetopt.generate_help(self, header=None)`

Generate help text (a list of strings, one per suggested line of
        output) from the option table for this FancyGetopt object.
        

<a name="FancyGetopt.get_attr_name_492310190"></a>
#### `FancyGetopt.get_attr_name(self, long_option)`

Translate long option name 'long_option' to the form it
        has as an attribute of some object: ie., translate hyphens
        to underscores.

<a name="FancyGetopt.get_option_order_504866980"></a>
#### `FancyGetopt.get_option_order(self)`

Returns the list of (option, value) tuples processed by the
        previous run of 'getopt()'.  Raises RuntimeError if
        'getopt()' hasn't been called yet.
        

<a name="FancyGetopt.getopt_726500129"></a>
#### `FancyGetopt.getopt(self, args=None, object=None)`

Parse command-line options in args. Store as attributes on object.

        If 'args' is None or not supplied, uses 'sys.argv[1:]'.  If
        'object' is None or not supplied, creates a new OptionDummy
        object, stores option values there, and returns a tuple (args,
        object).  If 'object' is supplied, it is modified in place and
        'getopt()' just returns 'args'; in both cases, the returned
        'args' is a modified copy of the passed-in 'args' list, which
        is left untouched.
        

<a name="FancyGetopt.has_option_1084693968"></a>
#### `FancyGetopt.has_option(self, long_option)`

Return true if the option table for this parser has an
        option with long name 'long_option'.

<a name="FancyGetopt.print_help_152685416"></a>
#### `FancyGetopt.print_help(self, header=None, file=None)`

None

<a name="FancyGetopt.set_aliases_1841219157"></a>
#### `FancyGetopt.set_aliases(self, alias)`

Set the aliases for this option parser.

<a name="FancyGetopt.set_negative_aliases_1579428126"></a>
#### `FancyGetopt.set_negative_aliases(self, negative_alias)`

Set the negative aliases for this option parser.
        'negative_alias' should be a dictionary mapping option names to
        option names, both the key and value must already be defined
        in the option table.

<a name="FancyGetopt.set_option_table_1638126737"></a>
#### `FancyGetopt.set_option_table(self, option_table)`

None

<a name="distutils.fancy_getopt.OptionDummy_1103708956"></a>
### distutils.fancy_getopt.OptionDummy(self, options=[])

Dummy class just used as a place to hold command-line option
    values as instance attributes.

<a name="OptionDummy.__init___663412451"></a>
#### `OptionDummy.__init__(self, options=[])`

Create a new OptionDummy instance.  The attributes listed in
        'options' will be initialized to None.

<a name="distutils.log_880671927"></a>
## distutils.log

<a name="distutils.log.Log_1791316898"></a>
### distutils.log.Log(self, threshold=3)

None

<a name="Log.__init___96795857"></a>
#### `Log.__init__(self, threshold=3)`

None

<a name="Log._log_853726519"></a>
#### `Log._log(self, level, msg, args)`

None

<a name="Log.debug_153411802"></a>
#### `Log.debug(self, msg, *args)`

None

<a name="Log.error_1972683729"></a>
#### `Log.error(self, msg, *args)`

None

<a name="Log.fatal_1545660352"></a>
#### `Log.fatal(self, msg, *args)`

None

<a name="Log.info_462281130"></a>
#### `Log.info(self, msg, *args)`

None

<a name="Log.log_548674238"></a>
#### `Log.log(self, level, msg, *args)`

None

<a name="Log.warn_252498183"></a>
#### `Log.warn(self, msg, *args)`

None

<a name="distutils.util_1394263673"></a>
## distutils.util

<a name="distutils.util.Mixin2to3_599796225"></a>
### distutils.util.Mixin2to3(self, /, *args, **kwargs)

Mixin class for commands that run 2to3.
    To configure 2to3, setup scripts may either change
    the class variables, or inherit from individual commands
    to override how 2to3 is invoked.

<a name="Mixin2to3.run_2to3_1700750410"></a>
#### `Mixin2to3.run_2to3(self, files)`

None

