# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# Hook for voo_evasion: https://pypi.org/project/voo-evasion/

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = collect_data_files('voo_evasion')
