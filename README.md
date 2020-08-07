# Extension Finder

Attempts to find installed browser extensions (sometimes called add-ons or plug-ins, depending on the browser).

## Features
Lists all available information for a given extension. Currently supports:

* Chrome
* Internet Explorer (Windows Only)
* Mozilla Firefox

All features were tested on Windows 8.1 and MacOSX 10.11


## Usage

Just run `extension_finder.py` from within the virtual environment.


$ python extension_finder.py

version    name                                    id
---------  --------------------------------------  --------------------------------
0.1        Chrome                                  mgndgikekgjfcpckkfioiadnlibdjbkf
1.0.1      Cisco WebEx Extension                   jlhmfgmfgeifomenelglieieghnjghma
14.1       Google Drive                            apdfllckaahabafndbhieahigkjlhalf
0.2.3      Spotify - Music for every moment        cnkjkdjlofllcpbemipjbcpfnglbgieh
0.2        Web Store                               ahfgeienlihckogmohjhadlkjgocpleb
3.0.15     Readability                             oknpjjbmpnndlpmnhmekjpocelpnlfdi
1.1        Google Sheets                           felcaaldnbdncclmgdcncolpebgiejap
1.2.0      Google Hangouts                         nkeimhogjdpnpccoofpliimaahmaaome
1.0        Google Network Speech                   neajdppkdcdipfabeoofebfddakdcjhd
0.9.38     CryptoTokenExtension                    kmendfapggjehodndflmmgagdbamhnfd
                                                   bepbmhgboaologfdajaanbcjmnhjmhfn
0.0.1.4    Hotword triggering                      nbpagnldghgfoolbancepceaanlmhfmd
0.1        Cloud Print                             mfehgcgbbipciphmccgaenjidiccnmng
34         feedly                                  hipbfijinpcgfogaopmgehiegacbhmob
1.0.8      Evernote Web                            lbfehkoinhhcknnbdgnnmjhiladcgbol
1.0        Feedback                                gfdkimpbcpahaombhbimeihdjnejgicl
1.4        Google Docs Offline                     ghbmnnjooekpmoecnnnilnnbdlolhkhi
2.0.6      Google Translate                        aapbdbdomjkkjkaonfhkkikfgjllcleb
0.9        Google Slides                           aapocclcgogkmnckokdopfmhonfmgoek
1          Chrome PDF Viewer                       mhjfbmdgcfjbbpaeojofohoefgiehjai
0.1        Bookmark Manager                        eemcgdkfndhakfknompkggombfjjjeno
0.2        Settings                                ennkphjdgehloodpbhlhldgbnhmacadg
0.0.1      GaiaAuthExtension                       mfffpogegjflfpflabcdkioaeobkgjik
8.1        Gmail                                   pjkljhegncpnkpknbcohdijeoejaedia
0.0.0.30   Google Search                           coobgpohoikkiipiblmjeljniedjpjpf
1.0.0.0    Chrome Web Store Payments               nmmhkkegccagdldgiimedpiccmgmieda
1.0.3      Slack                                   jeogkiiogjbmhklcnbgkdcjoioegiknm
4.2.8      YouTube                                 blpcfgokakmgnkcojhhkbfbldkacnbeo
0.9        Google Docs                             aohghmighlieiainnegkcijnfilokake
```

Since not everyone uses Python on Windows, there is also a `FindIEExtensions.ps1` PowerShell script. To run it simply:

```
PS C:\Users\User\Desktop\extension_finder> .\FindIEExtensions.ps1

DLL                                                                Name                                          CLSID
---                                                                ----                                          -----
C:\Windows\System32\ieframe.dll                                    Microsoft Url Search Hook                     {CFBFAE00-17A...
C:\Windows\System32\msxml3.dll                                     XML DOM Document                              {2933BF90-7B3...
C:\Windows\System32\Macromed\Flash\Flash.ocx                       Shockwave Flash Object                        {D27CDB6E-AE6...
C:\Windows\Downloaded Program Files\ieatgpc.dll                    GpcContainer Class                            {E06E2E99-0AA...
C:\Program Files\Microsoft Office\Office15\ONBttnIE.dll            Send to OneNote from Internet Explorer button {48E73304-E1D...
C:\Program Files\Microsoft Office\Office15\ONBttnIELinkedNotes.dll Linked Notes button                           {FFFDC614-B69...
```
