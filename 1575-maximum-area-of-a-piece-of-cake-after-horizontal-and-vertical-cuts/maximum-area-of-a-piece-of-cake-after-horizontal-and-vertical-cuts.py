class Solution:
    def maxArea(self, h, w, hc, vc):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """

        ret = 0

        if len(hc) == 0:
            if len(vc) == 0:
                return h*w

        hc.sort()
        vc.sort()

        hdiff = 0
        vdiff = 0
        lh = 0
        lv = 0

        for i in hc:
            if i-lh > hdiff:
                hdiff = i-lh
            lh = i
        if h-lh > hdiff:
            hdiff = h-lh

        for j in vc:
            if j-lv > vdiff:
                vdiff = j-lv
            lv = j
        if w-lv > vdiff:
            vdiff = w-lv

        return vdiff*hdiff % (10**9+7)