import pefile

pe = pefile.PE('main.exe')

with open('block_info.txt', 'w') as f:
    for section in pe.sections:
        f.write('Section name: {}\n'.format(section.Name.decode().rstrip('\x00')))
        f.write('Virtual Address: {}\n'.format(hex(section.VirtualAddress)))
        f.write('Virtual Size: {}\n'.format(hex(section.Misc_VirtualSize)))
        f.write('Raw Size: {}\n'.format(hex(section.SizeOfRawData)))
        f.write('Raw Data Offset: {}\n'.format(hex(section.PointerToRawData)))
        f.write('\n')
    f.close()