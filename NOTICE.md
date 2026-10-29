# Upstream attribution

This repository contains build notes, patches, and small scripts only. It does not contain game files, OnlineFix binaries, or proprietary binaries.

The patches are derived from the following upstream projects and remain subject to their respective licenses:

- **DWProton** — https://dawn.wine/dawn-winery/dwproton
- **Proton** — https://github.com/ValveSoftware/Proton
- **Wine** — https://gitlab.winehq.org/wine/wine
- **GE-Proton** — https://github.com/GloriousEggroll/proton-ge-custom
- **FFmpeg** — https://ffmpeg.org/

The `wine-media-rework.patch` file is a combined diff of the GE-Proton 11-6 `patches/ge-video-rework` series applied to Valve Wine 11.0 at commit `9358696fe9a2261329f4a83aa6a65fd436106154`, plus the minimal local compile fixes described in the changelog.

The scripts and documentation in this repository are provided as-is, without warranty. Redistribute or modify them only in compliance with the upstream licenses.
