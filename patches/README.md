# Patches

## `dwproton-ffmpeg-no-libvpx.patch`

Apply to the DWProton source before building:

```bash
git -C /path/to/dwproton apply dwproton-ffmpeg-no-libvpx.patch
```

This removes `--enable-libvpx` from `FFMPEG_CONFIGURE_ARGS`, preventing `libavcodec.so.62` from depending on `libvpx.so.9`, which is not shipped by the Proton runtime.

## `wine-media-rework.patch`

Apply to a clean **Valve Wine 11.0** checkout at:

```text
9358696fe9a2261329f4a83aa6a65fd436106154
```

```bash
git clone https://github.com/ValveSoftware/wine.git valve-wine
git -C valve-wine checkout 9358696fe9a2261329f4a83aa6a65fd436106154
git -C valve-wine apply wine-media-rework.patch
```

Then use that tree as DWProton's `wine` directory. It is based on GE-Proton 11-6's `patches/ge-video-rework` series and includes the minimal local fixes needed to compile it against this Wine base.
