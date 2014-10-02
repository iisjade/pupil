'''
(*)~----------------------------------------------------------------------------------
 Pupil - eye tracking platform
 Copyright (C) 2012-2014  Pupil Labs

 Distributed under the terms of the CC BY-NC-SA License.
 License details are in the file license.txt, distributed as part of this software.
----------------------------------------------------------------------------------~(*)
hello
'''
import platform

mac_plit_document_type_str = '''
<key>CFBundleDocumentTypes</key>
        <array>
            <dict>
            <key>CFBundleTypeExtensions</key>
            <array>
            <string>*</string>
            </array>
            <key>CFBundleTypeMIMETypes</key>
            <array>
            <string>*/*</string>
            </array>
            <key>CFBundleTypeName</key>
            <string>folder</string>
            <key>CFBundleTypeOSTypes</key>
            <array>
            <string>****</string>
            </array>
            <key>CFBundleTypeRole</key>
            <string>Viewer</string>
            </dict>
        </array>
'''

split_str = """
</dict>
</plist>"""

if platform.system() == 'Darwin':
    import shutil
    import write_version_file
    print "starting version stript:"
    write_version_file.main('dist/Pupil Player.app/Contents/MacOS')
    print "created version file in app dir"

    shutil.rmtree('dist/Pupil Player')
    print 'removed the non-app dist bundle'

    print "hack injecting file type info in to info.plist"
    with open("dist/Pupil Player.app/Contents/Info.plist", "r") as f:
        txt = f.read() # read everything in the file
    txt = txt.replace(split_str,mac_plit_document_type_str + split_str)
    with open("dist/Pupil Player.app/Contents/Info.plist", "w") as f:
        f.write(txt)


elif platform.system() == 'Linux':
    import sys,os
    import write_version_file
    import shutil

    distribtution_dir = 'dist'
    pupil_capture_dir =  os.path.join(distribtution_dir, 'pupil_player')


    shutil.copy('make_shortcut.sh',os.path.join(distribtution_dir,'make_shortcut.sh'))
    print "Copied a small script that creates a shortcut for the user into distribtution_dir"
    os.chmod(os.path.join(distribtution_dir,'make_shortcut.sh'),0775)
    print "Gave that file excetion rights"

    print "starting version stript:"
    write_version_file.main(pupil_capture_dir)
    print "created version file in dist folder"



