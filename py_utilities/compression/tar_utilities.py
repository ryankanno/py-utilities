#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import tarfile


def create_tarball(dirs_to_tarball, tarball_name, save_dir, gzip=True):

    utcnow = datetime.datetime.utcnow()

    if gzip:
        tar_opts = 'w:gz'
        file_suffix = 'tar.gz'
    else:
        tar_opts = 'w:'
        file_suffix = 'tar'

    tarball_filename = "{}_{}.{}".format(
        tarball_name,
        utcnow.strftime("%Y%m%d_%H%M%S"),
        file_suffix
    )

    tarball_filepath = os.path.join(save_dir, tarball_filename)

    with tarfile.open(tarball_filepath, tar_opts) as tar:
        for dir in dirs_to_tarball:
            tar.add(dir)
        return tarfile.is_tarfile(tarball_filepath)


# vim: filetype=python
