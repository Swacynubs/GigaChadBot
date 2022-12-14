FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2022-03-31-git-e301a24fa1-essentials_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/e301a24fa1

git-essentials build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
3DNow! enabled            yes
3DNow! extended enabled   yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
EBP available             yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
postprocessing support    yes
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
xmllint enabled           yes

External libraries:
avisynth                libopencore_amrnb       libvorbis
bzlib                   libopencore_amrwb       libvpx
gmp                     libopenjpeg             libwebp
gnutls                  libopenmpt              libx264
iconv                   libopus                 libx265
libaom                  librubberband           libxml2
libass                  libspeex                libxvid
libfontconfig           libsrt                  libzimg
libfreetype             libssh                  libzmq
libfribidi              libtheora               lzma
libgme                  libvidstab              mediafoundation
libgsm                  libvmaf                 sdl2
libmp3lame              libvo_amrwbenc          zlib

External libraries providing hardware acceleration:
amf                     d3d11va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec
cuvid                   libmfx

Libraries:
avcodec                 avformat                swresample
avdevice                avutil                  swscale
avfilter                postproc

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     flic                    pcm_u32be
aac_fixed               flv                     pcm_u32le
aac_latm                fmvc                    pcm_u8
aasc                    fourxm                  pcm_vidc
ac3                     fraps                   pcx
ac3_fixed               frwu                    pfm
acelp_kelvin            g2m                     pgm
adpcm_4xm               g723_1                  pgmyuv
adpcm_adx               g729                    pgssub
adpcm_afc               gdv                     pgx
adpcm_agm               gem                     photocd
adpcm_aica              gif                     pictor
adpcm_argo              gremlin_dpcm            pixlet
adpcm_ct                gsm                     pjs
adpcm_dtk               gsm_ms                  png
adpcm_ea                h261                    ppm
adpcm_ea_maxis_xa       h263                    prores
adpcm_ea_r1             h263i                   prosumer
adpcm_ea_r2             h263p                   psd
adpcm_ea_r3             h264                    ptx
adpcm_ea_xas            h264_cuvid              qcelp
adpcm_g722              h264_qsv                qdm2
adpcm_g726              hap                     qdmc
adpcm_g726le            hca                     qdraw
adpcm_ima_acorn         hcom                    qpeg
adpcm_ima_alp           hevc                    qtrle
adpcm_ima_amv           hevc_cuvid              r10k
adpcm_ima_apc           hevc_qsv                r210
adpcm_ima_apm           hnm4_video              ra_144
adpcm_ima_cunning       hq_hqa                  ra_288
adpcm_ima_dat4          hqx                     ralf
adpcm_ima_dk3           huffyuv                 rasc
adpcm_ima_dk4           hymt                    rawvideo
adpcm_ima_ea_eacs       iac                     realtext
adpcm_ima_ea_sead       idcin                   rl2
adpcm_ima_iss           idf                     roq
adpcm_ima_moflex        iff_ilbm                roq_dpcm
adpcm_ima_mtf           ilbc                    rpza
adpcm_ima_oki           imc                     rscc
adpcm_ima_qt            imm4                    rv10
adpcm_ima_rad           imm5                    rv20
adpcm_ima_smjpeg        indeo2                  rv30
adpcm_ima_ssi           indeo3                  rv40
adpcm_ima_wav           indeo4                  s302m
adpcm_ima_ws            indeo5                  sami
adpcm_ms                interplay_acm           sanm
adpcm_mtaf              interplay_dpcm          sbc
adpcm_psx               interplay_video         scpr
adpcm_sbpro_2           ipu                     screenpresso
adpcm_sbpro_3           jacosub                 sdx2_dpcm
adpcm_sbpro_4           jpeg2000                sga
adpcm_swf               jpegls                  sgi
adpcm_thp               jv                      sgirle
adpcm_thp_le            kgv1                    sheervideo
adpcm_vima              kmvc                    shorten
adpcm_xa                lagarith                simbiosis_imx
adpcm_yamaha            libaom_av1              sipr
adpcm_zork              libgsm                  siren
agm                     libgsm_ms               smackaud
aic                     libopencore_amrnb       smacker
alac                    libopencore_amrwb       smc
alias_pix               libopenjpeg             smvjpeg
als                     libopus                 snow
amrnb                   libspeex                sol_dpcm
amrwb                   libvorbis               sonic
amv                     libvpx_vp8              sp5x
anm                     libvpx_vp9              speedhq
ansi                    loco                    speex
ape                     lscr                    srgc
apng                    m101                    srt
aptx                    mace3                   ssa
aptx_hd                 mace6                   stl
arbc                    magicyuv                subrip
argo                    mdec                    subviewer
ass                     metasound               subviewer1
asv1                    microdvd                sunrast
asv2                    mimic                   svq1
atrac1                  mjpeg                   svq3
atrac3                  mjpeg_cuvid             tak
atrac3al                mjpeg_qsv               targa
atrac3p                 mjpegb                  targa_y216
atrac3pal               mlp                     tdsc
atrac9                  mmvideo                 text
aura                    mobiclip                theora
aura2                   motionpixels            thp
av1                     movtext                 tiertexseqvideo
av1_cuvid               mp1                     tiff
av1_qsv                 mp1float                tmv
avrn                    mp2                     truehd
avrp                    mp2float                truemotion1
avs                     mp3                     truemotion2
avui                    mp3adu                  truemotion2rt
ayuv                    mp3adufloat             truespeech
bethsoftvid             mp3float                tscc
bfi                     mp3on4                  tscc2
bink                    mp3on4float             tta
binkaudio_dct           mpc7                    twinvq
binkaudio_rdft          mpc8                    txd
bintext                 mpeg1_cuvid             ulti
bitpacked               mpeg1video              utvideo
bmp                     mpeg2_cuvid             v210
bmv_audio               mpeg2_qsv               v210x
bmv_video               mpeg2video              v308
brender_pix             mpeg4                   v408
c93                     mpeg4_cuvid             v410
cavs                    mpegvideo               vb
ccaption                mpl2                    vble
cdgraphics              msa1                    vc1
cdtoons                 mscc                    vc1_cuvid
cdxl                    msmpeg4v1               vc1_qsv
cfhd                    msmpeg4v2               vc1image
cinepak                 msmpeg4v3               vcr1
clearvideo              msnsiren                vmdaudio
cljr                    msp2                    vmdvideo
cllc                    msrle                   vmnc
comfortnoise            mss1                    vorbis
cook                    mss2                    vp3
cpia                    msvideo1                vp4
cri                     mszh                    vp5
cscd                    mts2                    vp6
cyuv                    mv30                    vp6a
dca                     mvc1                    vp6f
dds                     mvc2                    vp7
derf_dpcm               mvdv                    vp8
dfa                     mvha                    vp8_cuvid
dfpwm                   mwsc                    vp8_qsv
dirac                   mxpeg                   vp9
dnxhd                   nellymoser              vp9_cuvid
dolby_e                 notchlc                 vp9_qsv
dpx                     nuv                     vplayer
dsd_lsbf                on2avc                  vqa
dsd_lsbf_planar         opus                    wavpack
dsd_msbf                paf_audio               wcmv
dsd_msbf_planar         paf_video               webp
dsicinaudio             pam                     webvtt
dsicinvideo             pbm                     wmalossless
dss_sp                  pcm_alaw                wmapro
dst                     pcm_bluray              wmav1
dvaudio                 pcm_dvd                 wmav2
dvbsub                  pcm_f16le               wmavoice
dvdsub                  pcm_f24le               wmv1
dvvideo                 pcm_f32be               wmv2
dxa                     pcm_f32le               wmv3
dxtory                  pcm_f64be               wmv3image
dxv                     pcm_f64le               wnv1
eac3                    pcm_lxf                 wrapped_avframe
eacmv                   pcm_mulaw               ws_snd1
eamad                   pcm_s16be               xan_dpcm
eatgq                   pcm_s16be_planar        xan_wc3
eatgv                   pcm_s16le               xan_wc4
eatqi                   pcm_s16le_planar        xbin
eightbps                pcm_s24be               xbm
eightsvx_exp            pcm_s24daud             xface
eightsvx_fib            pcm_s24le               xl
escape124               pcm_s24le_planar        xma1
escape130               pcm_s32be               xma2
evrc                    pcm_s32le               xpm
exr                     pcm_s32le_planar        xsub
fastaudio               pcm_s64be               xwd
ffv1                    pcm_s64le               y41p
ffvhuff                 pcm_s8                  ylc
ffwavesynth             pcm_s8_planar           yop
fic                     pcm_sga                 yuv4
fits                    pcm_u16be               zero12v
flac                    pcm_u16le               zerocodec
flashsv                 pcm_u24be               zlib
flashsv2                pcm_u24le               zmbv

Enabled encoders:
a64multi                hevc_qsv                pcm_u24be
a64multi5               huffyuv                 pcm_u24le
aac                     jpeg2000                pcm_u32be
aac_mf                  jpegls                  pcm_u32le
ac3                     libaom_av1              pcm_u8
ac3_fixed               libgsm                  pcm_vidc
ac3_mf                  libgsm_ms               pcx
adpcm_adx               libmp3lame              pfm
adpcm_argo              libopencore_amrnb       pgm
adpcm_g722              libopenjpeg             pgmyuv
adpcm_g726              libopus                 png
adpcm_g726le            libspeex                ppm
adpcm_ima_alp           libtheora               prores
adpcm_ima_amv           libvo_amrwbenc          prores_aw
adpcm_ima_apm           libvorbis               prores_ks
adpcm_ima_qt            libvpx_vp8              qtrle
adpcm_ima_ssi           libvpx_vp9              r10k
adpcm_ima_wav           libwebp                 r210
adpcm_ima_ws            libwebp_anim            ra_144
adpcm_ms                libx264                 rawvideo
adpcm_swf               libx264rgb              roq
adpcm_yamaha            libx265                 roq_dpcm
alac                    libxvid                 rpza
alias_pix               ljpeg                   rv10
amv                     magicyuv                rv20
apng                    mjpeg                   s302m
aptx                    mjpeg_qsv               sbc
aptx_hd                 mlp                     sgi
ass                     movtext                 smc
asv1                    mp2                     snow
asv2                    mp2fixed                sonic
avrp                    mp3_mf                  sonic_ls
avui                    mpeg1video              speedhq
ayuv                    mpeg2_qsv               srt
bitpacked               mpeg2video              ssa
bmp                     mpeg4                   subrip
cfhd                    msmpeg4v2               sunrast
cinepak                 msmpeg4v3               svq1
cljr                    msvideo1                targa
comfortnoise            nellymoser              text
dca                     opus                    tiff
dfpwm                   pam                     truehd
dnxhd                   pbm                     tta
dpx                     pcm_alaw                ttml
dvbsub                  pcm_bluray              utvideo
dvdsub                  pcm_dvd                 v210
dvvideo                 pcm_f32be               v308
eac3                    pcm_f32le               v408
exr                     pcm_f64be               v410
ffv1                    pcm_f64le               vc2
ffvhuff                 pcm_mulaw               vorbis
fits                    pcm_s16be               vp9_qsv
flac                    pcm_s16be_planar        wavpack
flashsv                 pcm_s16le               webvtt
flashsv2                pcm_s16le_planar        wmav1
flv                     pcm_s24be               wmav2
g723_1                  pcm_s24daud             wmv1
gif                     pcm_s24le               wmv2
h261                    pcm_s24le_planar        wrapped_avframe
h263                    pcm_s32be               xbm
h263p                   pcm_s32le               xface
h264_amf                pcm_s32le_planar        xsub
h264_mf                 pcm_s64be               xwd
h264_nvenc              pcm_s64le               y41p
h264_qsv                pcm_s8                  yuv4
hevc_amf                pcm_s8_planar           zlib
hevc_mf                 pcm_u16be               zmbv
hevc_nvenc              pcm_u16le

Enabled hwaccels:
av1_d3d11va             hevc_nvdec              vc1_nvdec
av1_d3d11va2            mjpeg_nvdec             vp8_nvdec
av1_dxva2               mpeg1_nvdec             vp9_d3d11va
av1_nvdec               mpeg2_d3d11va           vp9_d3d11va2
h264_d3d11va            mpeg2_d3d11va2          vp9_dxva2
h264_d3d11va2           mpeg2_dxva2             vp9_nvdec
h264_dxva2              mpeg2_nvdec             wmv3_d3d11va
h264_nvdec              mpeg4_nvdec             wmv3_d3d11va2
hevc_d3d11va            vc1_d3d11va             wmv3_dxva2
hevc_d3d11va2           vc1_d3d11va2            wmv3_nvdec
hevc_dxva2              vc1_dxva2

Enabled parsers:
aac                     dvbsub                  mpegvideo
aac_latm                dvd_nav                 opus
ac3                     dvdsub                  png
adx                     flac                    pnm
amr                     g723_1                  rv30
av1                     g729                    rv40
avs2                    gif                     sbc
avs3                    gsm                     sipr
bmp                     h261                    tak
cavsvideo               h263                    vc1
cook                    h264                    vorbis
cri                     hevc                    vp3
dca                     ipu                     vp8
dirac                   jpeg2000                vp9
dnxhd                   mjpeg                   webp
dolby_e                 mlp                     xbm
dpx                     mpeg4video              xma
dvaudio                 mpegaudio

Enabled demuxers:
aa                      hnm                     pcm_f64le
aac                     ico                     pcm_mulaw
aax                     idcin                   pcm_s16be
ac3                     idf                     pcm_s16le
ace                     iff                     pcm_s24be
acm                     ifv                     pcm_s24le
act                     ilbc                    pcm_s32be
adf                     image2                  pcm_s32le
adp                     image2_alias_pix        pcm_s8
ads                     image2_brender_pix      pcm_u16be
adx                     image2pipe              pcm_u16le
aea                     image_bmp_pipe          pcm_u24be
afc                     image_cri_pipe          pcm_u24le
aiff                    image_dds_pipe          pcm_u32be
aix                     image_dpx_pipe          pcm_u32le
alp                     image_exr_pipe          pcm_u8
amr                     image_gem_pipe          pcm_vidc
amrnb                   image_gif_pipe          pjs
amrwb                   image_j2k_pipe          pmp
anm                     image_jpeg_pipe         pp_bnk
apc                     image_jpegls_pipe       pva
ape                     image_pam_pipe          pvf
apm                     image_pbm_pipe          qcp
apng                    image_pcx_pipe          r3d
aptx                    image_pgm_pipe          rawvideo
aptx_hd                 image_pgmyuv_pipe       realtext
aqtitle                 image_pgx_pipe          redspark
argo_asf                image_photocd_pipe      rl2
argo_brp                image_pictor_pipe       rm
argo_cvg                image_png_pipe          roq
asf                     image_ppm_pipe          rpl
asf_o                   image_psd_pipe          rsd
ass                     image_qdraw_pipe        rso
ast                     image_sgi_pipe          rtp
au                      image_sunrast_pipe      rtsp
av1                     image_svg_pipe          s337m
avi                     image_tiff_pipe         sami
avisynth                image_webp_pipe         sap
avr                     image_xbm_pipe          sbc
avs                     image_xpm_pipe          sbg
avs2                    image_xwd_pipe          scc
avs3                    imf                     scd
bethsoftvid             ingenient               sdp
bfi                     ipmovie                 sdr2
bfstm                   ipu                     sds
bink                    ircam                   sdx
binka                   iss                     segafilm
bintext                 iv8                     ser
bit                     ivf                     sga
bitpacked               ivr                     shorten
bmv                     jacosub                 siff
boa                     jv                      simbiosis_imx
brstm                   kux                     sln
c93                     kvag                    smacker
caf                     libgme                  smjpeg
cavsvideo               libopenmpt              smush
cdg                     live_flv                sol
cdxl                    lmlm4                   sox
cine                    loas                    spdif
codec2                  lrc                     srt
codec2raw               luodat                  stl
concat                  lvf                     str
dash                    lxf                     subviewer
data                    m4v                     subviewer1
daud                    matroska                sup
dcstr                   mca                     svag
derf                    mcc                     svs
dfa                     mgsts                   swf
dfpwm                   microdvd                tak
dhav                    mjpeg                   tedcaptions
dirac                   mjpeg_2000              thp
dnxhd                   mlp                     threedostr
dsf                     mlv                     tiertexseq
dsicin                  mm                      tmv
dss                     mmf                     truehd
dts                     mods                    tta
dtshd                   moflex                  tty
dv                      mov                     txd
dvbsub                  mp3                     ty
dvbtxt                  mpc                     v210
dxa                     mpc8                    v210x
ea                      mpegps                  vag
ea_cdata                mpegts                  vc1
eac3                    mpegtsraw               vc1t
epaf                    mpegvideo               vividas
ffmetadata              mpjpeg                  vivo
filmstrip               mpl2                    vmd
fits                    mpsub                   vobsub
flac                    msf                     voc
flic                    msnwc_tcp               vpk
flv                     msp                     vplayer
fourxm                  mtaf                    vqf
frm                     mtv                     w64
fsb                     musx                    wav
fwse                    mv                      wc3
g722                    mvi                     webm_dash_manifest
g723_1                  mxf                     webvtt
g726                    mxg                     wsaud
g726le                  nc                      wsd
g729                    nistsphere              wsvqa
gdv                     nsp                     wtv
genh                    nsv                     wv
gif                     nut                     wve
gsm                     nuv                     xa
gxf                     obu                     xbin
h261                    ogg                     xmv
h263                    oma                     xvag
h264                    paf                     xwma
hca                     pcm_alaw                yop
hcom                    pcm_f32be               yuv4mpegpipe
hevc                    pcm_f32le
hls                     pcm_f64be

Enabled muxers:
a64                     h264                    pcm_s24be
ac3                     hash                    pcm_s24le
adts                    hds                     pcm_s32be
adx                     hevc                    pcm_s32le
aiff                    hls                     pcm_s8
alp                     ico                     pcm_u16be
amr                     ilbc                    pcm_u16le
amv                     image2                  pcm_u24be
apm                     image2pipe              pcm_u24le
apng                    ipod                    pcm_u32be
aptx                    ircam                   pcm_u32le
aptx_hd                 ismv                    pcm_u8
argo_asf                ivf                     pcm_vidc
argo_cvg                jacosub                 psp
asf                     kvag                    rawvideo
asf_stream              latm                    rm
ass                     lrc                     roq
ast                     m4v                     rso
au                      matroska                rtp
avi                     matroska_audio          rtp_mpegts
avm2                    md5                     rtsp
avs2                    microdvd                sap
avs3                    mjpeg                   sbc
bit                     mkvtimestamp_v2         scc
caf                     mlp                     segafilm
cavsvideo               mmf                     segment
codec2                  mov                     smjpeg
codec2raw               mp2                     smoothstreaming
crc                     mp3                     sox
dash                    mp4                     spdif
data                    mpeg1system             spx
daud                    mpeg1vcd                srt
dfpwm                   mpeg1video              stream_segment
dirac                   mpeg2dvd                streamhash
dnxhd                   mpeg2svcd               sup
dts                     mpeg2video              swf
dv                      mpeg2vob                tee
eac3                    mpegts                  tg2
f4v                     mpjpeg                  tgp
ffmetadata              mxf                     truehd
fifo                    mxf_d10                 tta
fifo_test               mxf_opatom              ttml
filmstrip               null                    uncodedframecrc
fits                    nut                     vc1
flac                    obu                     vc1t
flv                     oga                     voc
framecrc                ogg                     w64
framehash               ogv                     wav
framemd5                oma                     webm
g722                    opus                    webm_chunk
g723_1                  pcm_alaw                webm_dash_manifest
g726                    pcm_f32be               webp
g726le                  pcm_f32le               webvtt
gif                     pcm_f64be               wsaud
gsm                     pcm_f64le               wtv
gxf                     pcm_mulaw               wv
h261                    pcm_s16be               yuv4mpegpipe
h263                    pcm_s16le

Enabled protocols:
async                   http                    rtmpe
cache                   httpproxy               rtmps
concat                  https                   rtmpt
concatf                 icecast                 rtmpte
crypto                  libsrt                  rtmpts
data                    libssh                  rtp
ffrtmpcrypt             libzmq                  srtp
ffrtmphttp              md5                     subfile
file                    mmsh                    tcp
ftp                     mmst                    tee
gopher                  pipe                    tls
gophers                 prompeg                 udp
hls                     rtmp                    udplite

Enabled filters:
abench                  dctdnoiz                owdenoise
abitscope               deband                  pad
acompressor             deblock                 pal100bars
acontrast               decimate                pal75bars
acopy                   deconvolve              palettegen
acrossfade              dedot                   paletteuse
acrossover              deesser                 pan
acrusher                deflate                 perms
acue                    deflicker               perspective
addroi                  deinterlace_qsv         phase
adeclick                dejudder                photosensitivity
adeclip                 delogo                  pixdesctest
adecorrelate            derain                  pixscope
adelay                  deshake                 pp
adenorm                 despill                 pp7
aderivative             detelecine              premultiply
adrawgraph              dialoguenhance          prewitt
adynamicequalizer       dilation                pseudocolor
adynamicsmooth          displace                psnr
aecho                   dnn_classify            pullup
aemphasis               dnn_detect              qp
aeval                   dnn_processing          random
aevalsrc                doubleweave             readeia608
aexciter                drawbox                 readvitc
afade                   drawgraph               realtime
afftdn                  drawgrid                remap
afftfilt                drawtext                removegrain
afifo                   drmeter                 removelogo
afir                    dynaudnorm              repeatfields
afirsrc                 earwax                  replaygain
aformat                 ebur128                 reverse
afreqshift              edgedetect              rgbashift
afwtdn                  elbg                    rgbtestsrc
agate                   entropy                 roberts
agraphmonitor           epx                     rotate
ahistogram              eq                      rubberband
aiir                    equalizer               sab
aintegral               erosion                 scale
ainterleave             estdif                  scale2ref
alatency                exposure                scale_cuda
alimiter                extractplanes           scale_qsv
allpass                 extrastereo             scdet
allrgb                  fade                    scharr
allyuv                  fftdnoiz                scroll
aloop                   fftfilt                 segment
alphaextract            field                   select
alphamerge              fieldhint               selectivecolor
amerge                  fieldmatch              sendcmd
ametadata               fieldorder              separatefields
amix                    fifo                    setdar
amovie                  fillborders             setfield
amplify                 find_rect               setparams
amultiply               firequalizer            setpts
anequalizer             flanger                 setrange
anlmdn                  floodfill               setsar
anlmf                   format                  settb
anlms                   fps                     shear
anoisesrc               framepack               showcqt
anull                   framerate               showfreqs
anullsink               framestep               showinfo
anullsrc                freezedetect            showpalette
apad                    freezeframes            showspatial
aperms                  fspp                    showspectrum
aphasemeter             gblur                   showspectrumpic
aphaser                 geq                     showvolume
aphaseshift             gradfun                 showwaves
apsyclip                gradients               showwavespic
apulsator               graphmonitor            shuffleframes
arealtime               grayworld               shufflepixels
aresample               greyedge                shuffleplanes
areverse                guided                  sidechaincompress
arnndn                  haas                    sidechaingate
asdr                    haldclut                sidedata
asegment                haldclutsrc             sierpinski
aselect                 hdcd                    signalstats
asendcmd                headphone               signature
asetnsamples            hflip                   silencedetect
asetpts                 highpass                silenceremove
asetrate                highshelf               sinc
asettb                  hilbert                 sine
ashowinfo               histeq                  smartblur
asidedata               histogram               smptebars
asoftclip               hqdn3d                  smptehdbars
aspectralstats          hqx                     sobel
asplit                  hstack                  spectrumsynth
ass                     hsvhold                 speechnorm
astats                  hsvkey                  split
astreamselect           hue                     spp
asubboost               huesaturation           sr
asubcut                 hwdownload              ssim
asupercut               hwmap                   stereo3d
asuperpass              hwupload                stereotools
asuperstop              hwupload_cuda           stereowiden
atadenoise              hysteresis              streamselect
atempo                  identity                subtitles
atilt                   idet                    super2xsai
atrim                   il                      superequalizer
avectorscope            inflate                 surround
avgblur                 interlace               swaprect
axcorrelate             interleave              swapuv
azmq                    join                    tblend
bandpass                kerndeint               telecine
bandreject              kirsch                  testsrc
bass                    lagfun                  testsrc2
bbox                    latency                 thistogram
bench                   lenscorrection          threshold
bilateral               libvmaf                 thumbnail
biquad                  life                    thumbnail_cuda
bitplanenoise           limitdiff               tile
blackdetect             limiter                 tinterlace
blackframe              loop                    tlut2
blend                   loudnorm                tmedian
bm3d                    lowpass                 tmidequalizer
boxblur                 lowshelf                tmix
bwdif                   lumakey                 tonemap
cas                     lut                     tpad
cellauto                lut1d                   transpose
channelmap              lut2                    treble
channelsplit            lut3d                   tremolo
chorus                  lutrgb                  trim
chromahold              lutyuv                  unpremultiply
chromakey               mandelbrot              unsharp
chromanr                maskedclamp             untile
chromashift             maskedmax               v360
ciescope                maskedmerge             vaguedenoiser
codecview               maskedmin               varblur
color                   maskedthreshold         vectorscope
colorbalance            maskfun                 vflip
colorchannelmixer       mcompand                vfrdet
colorcontrast           median                  vibrance
colorcorrect            mergeplanes             vibrato
colorhold               mestimate               vidstabdetect
colorize                metadata                vidstabtransform
colorkey                midequalizer            vif
colorlevels             minterpolate            vignette
colormatrix             mix                     vmafmotion
colorspace              monochrome              volume
colorspectrum           morpho                  volumedetect
colortemperature        movie                   vpp_qsv
compand                 mpdecimate              vstack
compensationdelay       mptestsrc               w3fdif
concat                  msad                    waveform
convolution             negate                  weave
convolve                nlmeans                 xbr
copy                    nnedi                   xcorrelate
cover_rect              noformat                xfade
crop                    noise                   xmedian
cropdetect              normalize               xstack
crossfeed               null                    yadif
crystalizer             nullsink                yadif_cuda
cue                     nullsrc                 yaepblur
curves                  oscilloscope            yuvtestsrc
datascope               overlay                 zmq
dblur                   overlay_cuda            zoompan
dcshift                 overlay_qsv             zscale

Enabled bsfs:
aac_adtstoasc           h264_redundant_pps      opus_metadata
av1_frame_merge         hapqa_extract           pcm_rechunk
av1_frame_split         hevc_metadata           prores_metadata
av1_metadata            hevc_mp4toannexb        remove_extradata
chomp                   imx_dump_header         setts
dca_core                mjpeg2jpeg              text2movsub
dump_extradata          mjpega_dump_header      trace_headers
dv_error_marker         mov2textsub             truehd_core
eac3_core               mp3_header_decompress   vp9_metadata
extract_extradata       mpeg2_metadata          vp9_raw_reorder
filter_units            mpeg4_unpack_bframes    vp9_superframe
h264_metadata           noise                   vp9_superframe_split
h264_mp4toannexb        null

Enabled indevs:
dshow                   lavfi
gdigrab                 vfwcap

Enabled outdevs:
sdl2
