---
title: '[Browser Test] New Spartan''s engine on IE 11 Technical Preview'
tags: []
id: '395'
categories:
  - - Computer Tips
date: 2015-01-26 22:31:06
---

Hello friends, today I would like to show you the test result of the new Spartan's engine on IE Technical Preview that came along with Windows 10 build 9926 (with Cortana and stuffs).

The test will be on 3 main browser: IE, Firefox and Chrome
<!-- more -->
The first test: SunSpider

IE: [Sun Spider of IE](http://www.webkit.org/perf/sunspider-1.0.2/sunspider-1.0.2/results.html?%7B%22v%22:%20%22sunspider-1.0.2%22,%20%223d-cube%22:%5B7,8,15,7,5,4,4,18,6,4%5D,%223d-morph%22:%5B1,1,3,1,1,1,1,3,1,1%5D,%223d-raytrace%22:%5B6,5,16,11,5,5,4,17,7,5%5D,%22access-binary-trees%22:%5B1,1,4,1,2,1,1,3,2,3%5D,%22access-fannkuch%22:%5B3,3,9,3,3,3,3,9,3,3%5D,%22access-nbody%22:%5B3,3,7,3,3,4,3,9,3,4%5D,%22access-nsieve%22:%5B1,1,3,1,1,1,1,3,1,1%5D,%22bitops-3bit-bits-in-byte%22:%5B0,0,2,0,0,0,0,2,0,0%5D,%22bitops-bits-in-byte%22:%5B1,1,3,1,1,1,1,3,1,1%5D,%22bitops-bitwise-and%22:%5B3,3,3,3,3,3,3,3,3,3%5D,%22bitops-nsieve-bits%22:%5B3,3,6,3,3,3,4,5,4,3%5D,%22controlflow-recursive%22:%5B1,1,4,1,1,1,1,4,1,1%5D,%22crypto-aes%22:%5B17,3,12,6,3,3,3,12,5,3%5D,%22crypto-md5%22:%5B1,1,9,1,2,1,1,8,1,1%5D,%22crypto-sha1%22:%5B1,1,7,1,1,1,1,7,1,1%5D,%22date-format-tofte%22:%5B8,8,13,9,7,7,7,13,8,7%5D,%22date-format-xparb%22:%5B15,14,16,14,13,13,13,15,13,15%5D,%22math-cordic%22:%5B2,1,4,2,2,1,2,3,2,2%5D,%22math-partial-sums%22:%5B9,6,11,9,6,6,7,11,8,7%5D,%22math-spectral-norm%22:%5B1,1,4,1,1,1,1,5,1,1%5D,%22regexp-dna%22:%5B9,9,9,9,9,8,9,8,8,8%5D,%22string-base64%22:%5B2,2,6,2,2,2,2,7,2,2%5D,%22string-fasta%22:%5B8,8,11,7,7,8,7,10,7,7%5D,%22string-tagcloud%22:%5B18,20,21,19,18,19,18,23,20,19%5D,%22string-unpack-code%22:%5B15,16,20,16,16,15,16,20,17,16%5D,%22string-validate-input%22:%5B7,6,9,6,6,6,6,9,6,6%5D%7D "Sun Spider of IE")

Firefox: [Sun Spider of Firefox](http://www.webkit.org/perf/sunspider-1.0.2/sunspider-1.0.2/results.html?%7B%22v%22:%20%22sunspider-1.0.2%22,%20%223d-cube%22:%5B134,132,142,143,134,141,137,148,139,140%5D,%223d-morph%22:%5B206,230,190,190,193,189,202,196,191,193%5D,%223d-raytrace%22:%5B177,177,184,177,178,177,191,186,178,190%5D,%22access-binary-trees%22:%5B124,112,116,124,112,123,126,122,113,113%5D,%22access-fannkuch%22:%5B408,478,411,419,408,440,416,415,428,411%5D,%22access-nbody%22:%5B233,272,239,245,234,235,234,238,241,247%5D,%22access-nsieve%22:%5B118,127,112,115,115,119,114,112,111,110%5D,%22bitops-3bit-bits-in-byte%22:%5B80,86,79,88,81,86,90,83,82,101%5D,%22bitops-bits-in-byte%22:%5B105,130,117,108,105,108,105,112,105,105%5D,%22bitops-bitwise-and%22:%5B341,371,349,333,349,330,351,348,342,356%5D,%22bitops-nsieve-bits%22:%5B151,152,147,158,146,156,151,152,150,147%5D,%22controlflow-recursive%22:%5B79,74,72,72,75,72,75,70,75,77%5D,%22crypto-aes%22:%5B144,149,149,144,157,145,143,145,145,152%5D,%22crypto-md5%22:%5B70,71,79,70,70,71,73,70,71,70%5D,%22crypto-sha1%22:%5B73,74,75,81,74,77,77,74,75,73%5D,%22date-format-tofte%22:%5B85,85,88,90,88,88,87,86,91,86%5D,%22date-format-xparb%22:%5B54,56,56,55,60,59,61,56,55,57%5D,%22math-cordic%22:%5B183,191,185,186,183,193,198,197,184,195%5D,%22math-partial-sums%22:%5B136,138,136,139,152,147,144,136,135,162%5D,%22math-spectral-norm%22:%5B81,79,87,81,87,98,79,79,81,83%5D,%22regexp-dna%22:%5B105,104,105,105,104,105,104,103,104,110%5D,%22string-base64%22:%5B92,97,94,94,92,92,97,98,94,96%5D,%22string-fasta%22:%5B119,120,117,122,116,118,118,119,117,128%5D,%22string-tagcloud%22:%5B92,78,74,78,80,75,83,90,76,85%5D,%22string-unpack-code%22:%5B102,110,106,99,105,104,108,103,100,102%5D,%22string-validate-input%22:%5B128,97,89,98,100,97,94,101,102,120%5D%7D "Sun Spider of Firefox")

Chrome: [Sun Spider of Chrome](https://www.webkit.org/perf/sunspider-1.0.2/sunspider-1.0.2/results.html?%7B%22v%22:%20%22sunspider-1.0.2%22,%20%223d-cube%22:%5B28,28,52,76,27,28,24,44,29,32%5D,%223d-morph%22:%5B87,94,47,69,57,49,68,38,52,58%5D,%223d-raytrace%22:%5B49,90,85,60,34,33,39,60,44,30%5D,%22access-binary-trees%22:%5B5,11,10,4,3,5,2,3,6,4%5D,%22access-fannkuch%22:%5B71,19,15,40,15,24,15,15,15,15%5D,%22access-nbody%22:%5B5,21,41,7,9,12,13,13,8,16%5D,%22access-nsieve%22:%5B8,6,8,6,6,5,7,5,7,10%5D,%22bitops-3bit-bits-in-byte%22:%5B3,6,19,2,3,3,2,7,3,2%5D,%22bitops-bits-in-byte%22:%5B9,65,35,9,9,10,12,8,20,9%5D,%22bitops-bitwise-and%22:%5B4,6,6,6,4,5,5,10,4,10%5D,%22bitops-nsieve-bits%22:%5B11,40,71,9,13,10,12,15,27,17%5D,%22controlflow-recursive%22:%5B40,5,10,4,5,3,8,3,3,5%5D,%22crypto-aes%22:%5B14,14,19,51,19,15,20,15,14,14%5D,%22crypto-md5%22:%5B61,28,43,16,16,27,16,12,19,16%5D,%22crypto-sha1%22:%5B13,15,14,38,14,22,22,14,25,19%5D,%22date-format-tofte%22:%5B64,30,52,24,23,24,23,33,26,25%5D,%22date-format-xparb%22:%5B29,67,20,74,28,21,22,37,18,28%5D,%22math-cordic%22:%5B30,10,48,10,12,12,14,11,18,11%5D,%22math-partial-sums%22:%5B87,115,94,77,41,47,33,33,34,56%5D,%22math-spectral-norm%22:%5B8,7,7,8,7,11,9,9,9,8%5D,%22regexp-dna%22:%5B16,40,21,75,23,22,16,18,15,17%5D,%22string-base64%22:%5B16,13,29,12,12,19,15,13,16,15%5D,%22string-fasta%22:%5B69,24,27,35,27,24,54,44,40,23%5D,%22string-tagcloud%22:%5B122,73,140,149,73,77,67,100,82,87%5D,%22string-unpack-code%22:%5B89,106,97,68,70,70,71,55,71,63%5D,%22string-validate-input%22:%5B23,69,67,30,21,22,27,23,24,22%5D%7D "Sun Spider of Chrome")

For a better comparison, here it is:

Firefox vs IE (FROM: Firefox, TO: IE) TEST                   COMPARISON               FROM                 TO             DETAILS

\===============================================================================

\*\* TOTAL \*\*:           24.7x as fast     3645.6ms +/- 1.2%    147.6ms +/- 21.0%     significant

\===============================================================================

3d:                  30.0x as fast      518.5ms +/- 1.6%     17.3ms +/- 42.6%     significant cube:              17.8x as fast      139.0ms +/- 2.5%      7.8ms +/- 44.4%     significant morph:             141.4x as fast     198.0ms +/- 4.5%      1.4ms +/- 43.0%     significant raytrace:          22.4x as fast      181.5ms +/- 2.3%      8.1ms +/- 42.7%     significant

access:              76.8x as fast      899.0ms +/- 2.7%     11.7ms +/- 38.4%     significant binary-trees:      62.4x as fast      118.5ms +/- 3.5%      1.9ms +/- 41.4%     significant fannkuch:          100.8x as fast     423.4ms +/- 3.6%      4.2ms +/- 43.0%     significant nbody:             57.6x as fast      241.8ms +/- 3.4%      4.2ms +/- 35.7%     significant nsieve:            82.4x as fast      115.3ms +/- 3.1%      1.4ms +/- 43.0%     significant

bitops:              81.6x as fast      693.6ms +/- 1.9%      8.5ms +/- 22.5%     significant 3bit-bits-in-byte: 214.0x as fast 85.6ms +/- 5.4% 0.4ms +/- 150.7% significant bits-in-byte:      78.6x as fast      110.0ms +/- 5.2%      1.4ms +/- 43.0%     significant bitwise-and:       115.7x as fast     347.0ms +/- 2.4%      3.0ms +/- 0.0%      significant nsieve-bits:       40.8x as fast      151.0ms +/- 1.8%      3.7ms +/- 20.5%     significant

controlflow:         46.3x as fast       74.1ms +/- 2.6%      1.6ms +/- 56.5%     significant recursive:         46.3x as fast       74.1ms +/- 2.6%      1.6ms +/- 56.5%     significant

crypto:              25.6x as fast      294.1ms +/- 1.2%     11.5ms +/- 58.6%     significant aes:               22.0x as fast      147.3ms +/- 2.2%      6.7ms +/- 54.4%     significant md5:               27.5x as fast       71.5ms +/- 2.8%      2.6ms +/- 86.1%     significant sha1:              34.2x as fast       75.3ms +/- 2.3%      2.2ms +/- 82.2%     significant

date:                6.33x as fast      144.3ms +/- 1.5%     22.8ms +/- 10.1%     significant format-tofte:      10.0x as fast       87.4ms +/- 1.6%      8.7ms +/- 19.4%     significant format-xparb:      4.04x as fast       56.9ms +/- 2.9%     14.1ms +/- 5.6%      significant

math:                35.2x as fast      415.5ms +/- 2.5%     11.8ms +/- 24.5%     significant cordic:            90.2x as fast      189.5ms +/- 2.3%      2.1ms +/- 29.8%     significant partial-sums:      17.8x as fast      142.5ms +/- 4.4%      8.0ms +/- 17.4%     significant spectral-norm:     49.1x as fast       83.5ms +/- 5.1%      1.7ms +/- 62.8%     significant

regexp:              12.2x as fast      104.9ms +/- 1.3%      8.6ms +/- 4.3%      significant dna:               12.2x as fast      104.9ms +/- 1.3%      8.6ms +/- 4.3%      significant

string:              9.32x as fast      501.6ms +/- 2.6%     53.8ms +/- 10.1%     significant base64:            32.6x as fast       94.6ms +/- 1.7%      2.9ms +/- 47.1%     significant fasta:             14.9x as fast      119.4ms +/- 2.1%      8.0ms +/- 12.6%     significant tagcloud:          4.16x as fast       81.1ms +/- 5.5%     19.5ms +/- 5.8%      significant unpack-code:       6.22x as fast      103.9ms +/- 2.4%     16.7ms +/- 7.8%      significant validate-input:    15.3x as fast      102.6ms +/- 8.4%      6.7ms +/- 13.4%     significant

Chrome vs IE (FROM: Chrome, TO: IE)

TEST                   COMPARISON               FROM                 TO             DETAILS

\===============================================================================

\*\* TOTAL \*\*:           5.19x as fast     766.5ms +/- 19.0%   147.6ms +/- 21.0%     significant

\===============================================================================

3d:                  8.73x as fast     151.1ms +/- 17.8%    17.3ms +/- 42.6%     significant cube:              4.72x as fast      36.8ms +/- 31.7%     7.8ms +/- 44.4%     significant morph:             44.2x as fast      61.9ms +/- 20.5%     1.4ms +/- 43.0%     significant raytrace:          6.47x as fast      52.4ms +/- 29.0%     8.1ms +/- 42.7%     significant

access:              4.36x as fast      51.0ms +/- 25.9%    11.7ms +/- 38.4%     significant binary-trees:      2.79x as fast       5.3ms +/- 40.2%     1.9ms +/- 41.4%     significant fannkuch:          5.81x as fast      24.4ms +/- 53.2%     4.2ms +/- 43.0%     significant nbody:             3.45x as fast      14.5ms +/- 51.3%     4.2ms +/- 35.7%     significant nsieve:            4.86x as fast       6.8ms +/- 16.3%     1.4ms +/- 43.0%     significant

bitops:              6.13x as fast      52.1ms +/- 53.4%     8.5ms +/- 22.5%     significant 3bit-bits-in-byte: 12.5x as fast 5.0ms +/- 74.4% 0.4ms +/- 150.7% significant bits-in-byte:      13.3x as fast      18.6ms +/- 70.4%     1.4ms +/- 43.0%     significant bitwise-and:       2.00x as fast       6.0ms +/- 26.9%     3.0ms +/- 0.0%      significant nsieve-bits:       6.08x as fast      22.5ms +/- 62.1%     3.7ms +/- 20.5%     significant

controlflow:         -                   8.6ms +/- 93.6%     1.6ms +/- 56.5% recursive:         -                   8.6ms +/- 93.6%     1.6ms +/- 56.5%

crypto:              5.61x as fast      64.5ms +/- 21.8%    11.5ms +/- 58.6%     significant aes:               2.91x as fast      19.5ms +/- 41.5%     6.7ms +/- 54.4%     significant md5:               9.77x as fast      25.4ms +/- 43.6%     2.6ms +/- 86.1%     significant sha1:              8.91x as fast      19.6ms +/- 28.2%     2.2ms +/- 82.2%     significant

date:                2.93x as fast      66.8ms +/- 24.0%    22.8ms +/- 10.1%     significant format-tofte:      3.72x as fast      32.4ms +/- 31.2%     8.7ms +/- 19.4%     significant format-xparb:      2.44x as fast      34.4ms +/- 41.3%    14.1ms +/- 5.6%      significant

math:                7.42x as fast      87.6ms +/- 28.9%    11.8ms +/- 24.5%     significant cordic:            8.38x as fast      17.6ms +/- 49.9%     2.1ms +/- 29.8%     significant partial-sums:      7.71x as fast      61.7ms +/- 34.2%     8.0ms +/- 17.4%     significant spectral-norm:     4.88x as fast       8.3ms +/- 10.8%     1.7ms +/- 62.8%     significant

regexp:              3.06x as fast      26.3ms +/- 50.5%     8.6ms +/- 4.3%      significant dna:               3.06x as fast      26.3ms +/- 50.5%     8.6ms +/- 4.3%      significant

string:              4.80x as fast     258.5ms +/- 14.7%    53.8ms +/- 10.1%     significant base64:            5.52x as fast      16.0ms +/- 22.6%     2.9ms +/- 47.1%     significant fasta:             4.59x as fast      36.7ms +/- 29.8%     8.0ms +/- 12.6%     significant tagcloud:          4.97x as fast      97.0ms +/- 21.9%    19.5ms +/- 5.8%      significant unpack-code:       4.55x as fast      76.0ms +/- 15.1%    16.7ms +/- 7.8%      significant validate-input:    4.90x as fast      32.8ms +/- 40.9%     6.7ms +/- 13.4%     significant

HTML  Test:

For HTML5, I don't have any reliable test. I use PeaceKeeper

IE: http://peacekeeper.futuremark.com/results?key=AHJR&resultId=5664056 - 1992

Chrome: http://peacekeeper.futuremark.com/results?key=AHJp&resultId=5664119 - 1490

Firefox: http://peacekeeper.futuremark.com/results?key=AHJq&resultId=5664118 - 850

CSS3 Test

For CSS3: I use http://css3test.com/

IE: 50%, "Determined by passing **614** tests out of **1416** total for **293** features"

Firefox: 57%, "Determined by passing **702** tests out of **1416** total for **293** features"

Chrome: 58%, "Determined by passing 730 tests out of 1416 total for 293 features"

Thanks for reading this