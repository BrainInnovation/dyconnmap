""" Sliding Window




"""
# Author: Avraam Marimpis <avraam.marimpis@gmail.com>

import numpy as np


def sliding_window(data, window_length=25, step=1, pairs=None):
    """

    """
    n_samples, n_rois = np.shape(data)

    n_slides = np.int32(np.ceil((n_samples - window_length) / step + 1.0))

    dfcg = np.zeros((n_slides, n_rois, n_rois))

    for slide in range(n_slides):
        offset1 = np.int32((slide) * step)
        offset2 = np.int32((slide) * step + window_length)

        sl = data[offset1:offset2, :]

        for k in range(n_rois):
            for l in range(k + 1, n_rois):
                pass

        print("{0}:{1} -> {2}".format(offset1, offset2, np.shape(sl)))

    return dfcg


def sliding_window_indx(data, window_length, overlap=0.75, pairs=None):
    """ Compute the indices and pairs using a sliding window.

    Slide a window over ``data``, and return the indices and offsets.


    Parameters
    ----------
    data : array-like, shape(n_channels, n_samples)
        Multichannel recording data.

    window_length : int
        Number of samples to be used in the computation of the connectivity.

    overlap : float
        Percentage of the ``window_length`` by which the window will overlap when
        sliding forward.

    pairs : array-like or `None`
        - If an `array-like` is given, notice that each element is a tuple of length two.
        - If `None` is passed, complete connectivity will be assumed.


    Returns
    -------
    indices: array - like, shape(n_windows, start_offset, end_offset, n_channels, n_channels)
        Indices of pairs.
    """
    n_channels, n_samples = np.shape(data)

    if window_length >= n_samples:
        raise Exception(
            "The size of window cannot be greater than the number of samples"
        )

    if overlap >= 0.99 or overlap <= 0.05:
        raise Exception("Illegal value for overlap parameter.")

    step = window_length - np.int32(window_length * overlap)
    windows = np.int32(np.round((n_samples - window_length) / step))

    indices = [
        (win_id, int(win_id * step), int(window_length + (win_id * step)), c1, c2)
        for win_id in range(windows)
        for c1 in range(0, n_channels)
        for c2 in range(c1, n_channels)
        if c1 != c2
    ]

    return indices
