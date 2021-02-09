import PySimpleGUIQt as sg

sg.theme('dark blue 2')
#dark blue 2
left_menu = sg.Column([
    [sg.Button('Home')],
    [sg.Button('Foo')],
    [sg.Button('Help')],
])

graph_col = [
    [sg.Graph((100, 100), (0, 0), (1, 1))],
    [sg.Graph((100, 100), (0, 0), (1, 1))]
]

main_col = [[sg.MultilineOutput('This is some text so see how the font looks that I am using.')]]

main_pane = sg.Column([
    [sg.Text('Progress'), sg.ProgressBar(100)],
    [sg.Col(graph_col), sg.Col(main_col)],
#    [sg.MultilineOutput()]
    ])

#layout = [[left_menu, main_pane]]
layout = [[main_pane]]

window = sg.Window('ml4all', layout, font='Helvetica 14', element_padding=(5, 5))
# Calibre Roboto Helvetica, Verdana

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):
        break
    elif event == 'OK':
        pass

print(window.QTApplication)
window.close()


"""
Available fonts on mac:
'.AppleSystemUIFont', '.AppleSystemUIFontMonospaced', 'Academy Engraved LET', 'Al Bayan', 'Al Nile', 'Al Tarikh', 'American Typewriter'
, 'Andale Mono', 'Apple Braille', 'Apple Chancery', 'Apple Color Emoji', 'Apple LiGothic', 'Apple LiSung', 'Apple SD Gothic Neo'
, 'Apple Symbols', 'AppleGothic', 'AppleMyungjo', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial Hebrew Scholar', 'Arial Narrow', 'Arial Rounded MT Bold',
 'Arial Unicode MS', 'Avenir', 'Avenir Next', 'Avenir Next Condensed', 'Ayuthaya', 'Baghdad', 'Baloo', 'Baloo Bhai', 'Baloo Bhaijaan', 'Baloo Bhaina', 
 'Baloo Chettan', 'Baloo Da', 'Baloo Paaji', 'Baloo Tamma', 'Baloo Tammudu', 'Baloo Thambi', 'Bangla MN', 'Bangla Sangam MN', 'Baoli SC', 'Baoli TC', 
 'Baskerville', 'Beirut', 'BiauKai', 'Big Caslon', 'Bodoni 72', 'Bodoni 72 Oldstyle', 'Bodoni 72 Smallcaps', 'Bodoni Ornaments', 'Bradley Hand', 
 'Brush Script MT', 'Cambay Devanagari', 'Chalkboard', 'Chalkboard SE', 'Chalkduster', 'Charter', 'Cochin', 'Comic Sans MS', 'Copperplate', 
 'Corsiva Hebrew', 'Courier', 'Courier New', 'Damascus', 'DecoType Naskh', 'Devanagari MT', 'Devanagari Sangam MN', 'Didot', 'DIN Alternate', 
 'DIN Condensed', 'Diwan Kufi', 'Diwan Thuluth', 'Euphemia UCAS', 'Farah', 'Farisi', 'Futura', 'Galvji', 'GB18030 Bitmap', 'Geeza Pro', 'Geneva', 
 'Georgia', 'Gill Sans', 'Gotu', 'Grantha Sangam MN', 'Gujarati MT', 'Gujarati Sangam MN', 'GungSeo', 'Gurmukhi MN', 'Gurmukhi MT', 'Gurmukhi Sangam MN', 
 'Hannotate SC', 'Hannotate TC', 'HanziPen SC', 'HanziPen TC', 'HeadLineA', 'Hei', 'Heiti SC', 'Heiti TC', 'Helvetica', 'Helvetica Neue', 'Herculanum', 
 'Hiragino Maru Gothic ProN', 'Hiragino Mincho ProN', 'Hiragino Sans', 'Hiragino Sans CNS', 'Hiragino Sans GB', 'Hoefler Text', 'Impact', 'InaiMathi', 
 'ITF Devanagari', 'ITF Devanagari Marathi', 'Jaini', 'Jaini Purva', 'Kai', 'Kailasa', 'Kaiti SC', 'Kaiti TC', 'Kannada MN', 'Kannada Sangam MN', 
 'Kefa', 'Khmer MN', 'Khmer Sangam MN', 'Klee', 'Kohinoor Bangla', 'Kohinoor Devanagari', 'Kohinoor Gujarati', 'Kohinoor Telugu', 'Kokonor', 'Krungthep', 
 'KufiStandardGK', 'Lahore Gurmukhi', 'Lantinghei SC', 'Lantinghei TC', 'Lao MN', 'Lao Sangam MN', 'Libian SC', 'Libian TC', 'LiHei Pro', 'LingWai SC', 
 'LingWai TC', 'LiSong Pro', 'Lucida Grande', 'Luminari', 'Maku', 'Malayalam MN', 'Malayalam Sangam MN', 'Marker Felt', 'Menlo', 'Microsoft Sans Serif', 
 'Mishafi', 'Mishafi Gold', 'Modak', 'Monaco', 'Mshtakan', 'Mukta', 'Mukta Mahee', 'Mukta Malar', 'Mukta Vaani', 'Muna', 'Myanmar MN', 'Myanmar Sangam MN', 
 'Nadeem', 'Nanum Brush Script', 'Nanum Gothic', 'Nanum Myeongjo', 'Nanum Pen Script', 'New Peninim MT', 'Noteworthy', 'Noto Nastaliq Urdu', 'Noto Sans Kannada', 
 'Noto Sans Myanmar', 'Noto Sans Oriya', 'Noto Serif Kannada', 'Noto Serif Myanmar', 'Optima', 'Oriya MN', 'Oriya Sangam MN', 'Osaka', 'Palatino', 'Papyrus', 
 'Party LET', 'PCMyungjo', 'Phosphate', 'PilGi', 'PingFang HK', 'PingFang SC', 'PingFang TC', 'Plantagenet Cherokee', 'PSL Ornanong Pro', 'PT Mono', 'PT Sans', 
 'PT Sans Caption', 'PT Sans Narrow', 'PT Serif', 'PT Serif Caption', 'Raanana', 'Rockwell', 'Sana', 'Sathu', 'Savoye LET', 'Shobhika', 'Shree Devanagari 714', 
 'SignPainter', 'Silom', 'Sinhala MN', 'Sinhala Sangam MN', 'Skia', 'Snell Roundhand', 'Songti SC', 'Songti TC', 'STFangsong', 'STHeiti', 'STIXGeneral', 
 'STIXIntegralsD', 'STIXIntegralsSm', 'STIXIntegralsUp', 'STIXIntegralsUpD', 'STIXIntegralsUpSm', 'STIXNonUnicode', 'STIXSizeFiveSym', 'STIXSizeFourSym', 
 'STIXSizeOneSym', 'STIXSizeThreeSym', 'STIXSizeTwoSym', 'STIXVariants', 'STKaiti', 'STSong', 'Sukhumvit Set', 'Symbol', 'Tahoma', 'Tamil MN', 'Tamil Sangam MN', 
 'Telugu MN', 'Telugu Sangam MN', 'Thonburi', 'Times', 'Times New Roman', 'Tiro Bangla', 'Tiro Gurmukhi', 'Tiro Hindi', 'Tiro Kannada', 'Tiro Marathi', 'Tiro Sanskrit', 
 'Tiro Tamil', 'Tiro Telugu', 'Toppan Bunkyu Gothic', 'Toppan Bunkyu Midashi Gothic', 'Toppan Bunkyu Midashi Mincho', 'Toppan Bunkyu Mincho', 'Trattatello', 
 'Trebuchet MS', 'Tsukushi A Round Gothic', 'Tsukushi B Round Gothic', 'Verdana', 'Waseem', 'Wawati SC', 'Wawati TC', 'Webdings', 'Weibei SC', 'Weibei TC', 
 'Wingdings', 'Wingdings 2', 'Wingdings 3', 'Xingkai SC', 'Xingkai TC', 'Yuanti SC', 'Yuanti TC', 'YuGothic', 'YuKyokasho', 'YuKyokasho Yoko', 'YuMincho', 
 'YuMincho +36p Kana', 'Yuppy SC', 'Yuppy TC', 'Zapf Dingbats', 'Zapfino'

"""