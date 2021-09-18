import sys
from help import ProgramUsage, License, Noise


def parse_commandline_args(argv):
    options = []
    inputs = []
    outputs = []

    idx = 1
    while (idx < len(argv)) and (argv[idx] not in ['-i', '--input', '-o', '--output', '-ox', '--output-pattern']):
        options.append(argv[idx])
        idx += 1

    while (idx < len(argv) - 1) and (argv[idx] in ['-i', '--input']):
        inputs.append(argv[idx + 1])
        idx += 2

    if (idx < len(argv) - 2) and argv[idx] in ['-ox', '--output-pattern']:
        outputs.append(argv[idx + 1])
    else:
        while (idx < len(argv) - 1) and (argv[idx]) in ['-o', '--output']:
            outputs.append(argv[idx + 1])
            idx += 2

    return options, inputs, outputs


def is_quiet(options):
    return ('-q' in options) or ('--quiet' in options)


def sanitize_options(options):
    is_assemble = '-a' in options or '--assemble' in options
    is_disassemble = '-d' in options or '--disassemble' in options

    dis_option_count = 0
    asm_option_count = 0

    for option in options:
        if option[0:6] == '--dump':
            dis_option_count += 1
        elif option[0:5] == '--asm':
            asm_option_count += 1

    if is_assemble and is_disassemble:
        return 'cannot use both "assemble" and "disassemble"'

    if is_assemble and dis_option_count is not 0:
        return 'cannot use disassembling option in assembling mode'

    if is_disassemble and asm_option_count is not 0:
        return 'cannot use assembling option in disassembling mode'

    return True


def application_start(argv, env):
    if len(argv) < 2:
        print(ProgramUsage)
        return -1

    if ('-h' in argv) or ('--help' in argv):
        print(ProgramUsage)
        return 0
    elif '--license' in argv:
        print(License)
        return 0
    else:
        options, inputs, outputs = parse_commandline_args(argv)
        quiet = is_quiet(options)

    if not quiet:
        print(Noise, file=sys.stderr)

    sanitize = sanitize_options(options)
    if sanitize is not True:
        if not quiet:
            print('fatal error: ' + sanitize, file=sys.stderr)
        return -1

    return 0
