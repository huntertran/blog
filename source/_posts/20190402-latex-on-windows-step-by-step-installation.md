---
title: '[Research] - LaTex on Windows - Step by step installation'
tags: []
id: '1134'
categories:
  - - Others
date: 2019-04-02 02:21:51
---

In this blog, I will instruct you on how to install and writing LaTex documents on Windows with ease.

*   [1. Requirement](#1-requirement)
    *   [1.1 List of software](#11-list-of-software)
    *   [1.2 Installing MikTex](#12-installing-miktex)
*   [2. Setup on Visual Studio Code](#2-setup-on-visual-studio-code)
*   [3. Writing on Visual Studio Code](#3-writing-on-visual-studio-code)
*   [4. Collaboration](#4-collaboration)
    *   [4.1 VSCode Live Share](#41-vscode-live-share)
    *   [4.2 Start Collaboration](#42-start-collaboration)
    *   [4.3 Join a shared collaboration session](#43-join-a-shared-collaboration-session)
    *   [4.4 Live Share Maximum collaborators](#44-live-share-maximum-collaborators)
<!-- more -->
# 1. Requirement

## 1.1 List of software

First thing first, you would need to download and install a series of software.

> Choose the correct version with your windows (x86/x64)

1.  [StrawberryPerl](http://strawberryperl.com/)
2.  [Visual Studio Code (text editor, not confused with Visual Studio IDE)](https://code.visualstudio.com/download)
3.  [MikTex](https://miktex.org/download) (easier to install and use)

> For me, MikTex is kinda difficult to download. The server close connection every 30-45 secs. If this happened to you, use a download manager. For example: [Free Download Manager](http://www.freedownloadmanager.org/download.htm)

## 1.2 Installing MikTex

Accept all default option, and wait for the installation completed.

Start > MikTex Console > Updates > Check for updates

![Update MikTex Packages](https://lh3.googleusercontent.com/hKiTMvw_chg0MzcT0UenM6z1M7zU7NJJkLop9Nq_5nVy_SUeN7BpS9j1mvLERjMfhBcRzcnu5New9thPpx4IRuByXO7RNijbkJbkCbQTisLSO4tqgWPQFHzE50hI13XjwCCYsQYiiA=w2400)

> In case of difficult in download packages, you can change 'Install from' option with a `http` repository

Install `latexmk` package

![latexmk](https://lh3.googleusercontent.com/Wr5yvLr37Tn5pQgda46K2EfUTKFw9qwWkZ0iJFs0Fpi7AJSB_iMFWqE80T3-CqE_r_WdT2RIdho2gvxZqOPu27sinQtqjon5dS2zf_L_gFvS33haw-KRnPfipks2rqMevPaWb1UeoycVx44tAsHuLps5AefKa2PP2Mx7-mItHFd0cYKIPqyy98QpDlypjQmGnsszKzdJ2IOrl3TmIK38kn7ESKPczK4FNN1UKLWfijqySHZ6aUoVWcsM3X4T7cJiFiuD-Mxazoxh5Y8QOWLkA2705VLniHlt_0D8U0WzG-TvVLvr0O2TS5m5i1FTpY5iis55MgF1isyDDzPZ6xUQ2UX15lAv4XCDuzhJP-BiNXb3eDArLDoynxUQv3gTDY8myBwIPhWGtnMcsB2QHyQkwXuEQyftQG4KKUeiYRjmq1g3uM8FXLvT949MnggObXdDewcnI3gnnbmoSEK2FCFyue10QnJbR9Ks0LAnZDfvDvW0fL0F9HSm5yw7C4wNeZskGxBqAWn-f2sy7tX1twEOYcy9QVJcHJ2V1I-6Th_7OCn86OdPePRgopd1FCTPfetLy0pDlyrfIAxWvC2Eiycooqn0WEsmxpojP4QiZhteO-2EMKQYdMluHP-e_51Zf7OR0LRVjftUOntg5XYFWE55bsbrmyyowbI3SpYBt4b51juG_JwMkQmnyYtVTF4u_Q7SjikShzZRNbvPsDoRUTk3irKH=w802-h632-no)

# 2. Setup on Visual Studio Code

If you are opening Visual Studio Code while installing MikTex and Perl ActiveState, please CLOSE Visual Studio Code and open it again.

Open Extension > search for Latex > Install LaTeX Workshop

![LaTeX Workshop](https://lh3.googleusercontent.com/vr8qIvd2Bz3tT0srcGXASblQHtvInX_cZKZtugGzLfZ71TbWWb3ddmAaHDpuSCO3Rz18KzyYuOBdX15Pgn_7p47EohvqiVCyJ8Ygur8qE9XI5cGeAk6nEMgLuyh2iVy1oIddau0iIbFLSxr6QvpJeT8HFrVD7P4ljDhKOLeBY72uyuEBBZjiqjrm5BIT21h2qZzqG0E-mytMi747yK98kwYUay3cec0uEX3ShVJIr8ffYfTAS17tQ5QdA0zpcql8Kc7yTWpsPMrN-5lCJQYlQnmH5-5AVxlugLVB956LMKXGuj22OUWHv3BpxJvTMPq0GzlvnTbRDhRLLUji-WlTU8rhHlRtbCGBb3SZjt-8aNAPLBtAoGRYWbSEpQiZILwslexygTxsMrkUmarXlfGJONKWt94c4vyFmwLlln8DdGB5ER3R8njYaH1RFxHnUBYAz2mOGuMDkY2_jAxQo1vLW0ftf1bQGEE0SddAnBUoj87n7lbULZi_q2bOJLUfgMn2JHGJq225OeD5oADbhCyJq4cMWTD9xqxS1YG6KGBH_1LWlyOyVd61aHob2UJa_Bh_YJR4fGg-LX2qB8XIHg3pl06rYLFmhSXlACOPYsyW7O3OORa0qcDKhgnzJS-LnXCndxbpOzM42R9lLCcCIkt558-TYaqKUDB0Lx8mc1IiQ4Mp49U6cbjQHbc6CMUe9z23nH3iCfdn_a0ASOuAICKCQi5Y=w699-h488-no)

# 3. Writing on Visual Studio Code

It is recommended to create a folder for each LaTeX document (to store images, charts, data file, etc).

Open that folder with Visual Studio Code, create a new file ended with `.tex`

Open that `.tex` file, then you can start playing with your LaTeX

![writing latex](https://lh3.googleusercontent.com/lT5SSLoB-mNXiVL8N9szGf5l36w1u4LgxK2JwSCFKiZFgXXF8Og17FuYaBwcCHZogn_ut-aymvoJRn-3yKgF0f6PGREaNym8ZH0kwvPHA6_wqSRBo1xO5cZQd3th8kQd9MogtWLPN6fFCNk-ww8gUiZQNxhYnvG0c4ASCePogPFb-ldilXV-RoM5VSUShrxRBicNTIenJ2jAFAsNf9Pd-HXeGz1iYEXcEEo7aU14__e1v_8UHlm6d1SqvdTdta-xuvrvI59MGW9eGrCWbsC0mX7EDKQkIUX1G5FzESvSEEEw5VYzr37GdRygooETBAaiJdAwaPG3IT1BtBYc3sRxv6xdZc-iyQZUdWJQb1FqUtJtckMME89NtQ7DlOvwv-2wpR3N9dagmKvirRH95ZOtG8iDkWSmjxpW1cXNGBfCw4WkwvnVMNSlgR6-rOpvX9osE0MbaaTLQNfRsCimqjYaMUu8_N26u1oEBoGc6jrrCD2kNtMO2kFI8nS9eF6YASftwF9mMCqpSouWOfjsMjhVeD5XNoaAFEPa3AMaoXXlYD_k7G8V1TmFT1D9IX4umcw1domD1iZNddrf79tvToTCL4dBS7C-jrRh4F22MgFTd5Ga_6woKz9t1Gk7WR3iytTbsO7s1s74BKjmRj97X80PHv5czTvCIMICUTGZ3iZKDvQVTmrRiIw0OEiWmMXSqvod44viPo9dtDfDdQFPiEFXEoOn=w594-h316-no)

To preview the rendered PDF, you can click on small icon on the top-right corner

![preview PDF](https://lh3.googleusercontent.com/fxx75if3R_weAeIaewFsJMXOEKY0TCPuOius0tbqidi3sB-DU5hBsCY_vFNtEqr-4B0DoXGsPq649OIG_9pM6rh2X2UP8In9UQ6lH41vPrHkq3UwMMRKUcrJyO6w-XBoZvl1YeuwO4r9gzXv22JA4TdmWxbDCMi0x3l3DfCnTTaQYyhuxsBoE3iCg6-xfI2oK4rO8OH-12kHLZ0Uf08HhSolhLP01sxzwOiJs9jrUuM9UCa6CPHHF5bVOQa-llPz-ZNLZy8PZacU4orXOHQSr106PgKH-Jw10Lrd2RWBeNtoIziSyMPkG38z_g1wDhJRHBy1iC8Rs940URXh6EilLCIFEqRSAyu35_2znAqQ11MstXwkeTclgv3XGVZHbaMJkeKXneB6a0jMTUXdL6XyHrYBUUaEkNdoiV6GwimUPUICK9zAC8duUNK3y4di9s8X0ew-Ypjl396pUGh0GQudIYLkZwzvqxQNIgJ0-F2gh-8BscL9upPjpFgpVCOv1Ni6RpOY4kQLNkG1tH2hD_YqqO-NElntrxg_N_vVCY0JP7Oq-wy_GBw67EAtTugdPQYdHV1S0r8UUbPO4IgTo6tV5U9EnKaKklFjB7rx32Z5zoEGt2ATfuBS_2iDCfi40e8kJ3IL4PuL-219_25hr1abJrYeRQOaP83z2xAxoVadV-qG4Vn5pui6jFd9yuyPgXE2p7z1Q_Iq4d_S8nxzgcPIlXwU=w457-h215-no)

# 4. Collaboration

Okay okay, it's cool, but _**why**_ do I need to write LaTeX offline, using Visual Studio Code, instead of the awesome [Overleaf](https://www.overleaf.com)?

The answer is the price. For collaboration, overleaf offer 80 USD/year for 6 students (the price is higher if you don't have student account).

With visual studio code, it's free, and super fast too.

## 4.1 VSCode Live Share

Live Share is an amazing feature offered by Microsoft. It's not even share files, it's also share folders and projects.

To begin with, install VS Live Share extension

![Live Share](https://lh3.googleusercontent.com/o8pCg6t8GTje2dHSMWtpY2w8NDnUBn5bJwjLFt5FYlZQ-hG-Tqui1_0snN0_QEAAC5nNi7l0v7C2K4n7o6Op52-8VIihQ_npqYo2IzTcpvDQlatMwn3t7qzcaBylosda0bfRquUkCYG553lIi1xzmVVI63AbX00DEmpJIP3xWhEoxDUUOIFIu9WiJVsrIOKpSV4G2wKoJtT0UvVmSbi9KHEo_UW4_Q2vZu2zHNO3pxXOrov13GIwQpOjOQ9uEPnqlPglYJOomrFZJdP1bRlO9dwj1nBr_qs9xF81TIdiXxhhxahiI5rjkEnBZElHbTXbXNJ7giP4dKNRw_1bDC5fZ6Lkk4PIgDX6GYk6mfH0WH73rDzM-jMPRL0ndptmmQmgjws0n-EgZJNhxwO0otXNJb7_EMr228fyXNlD1qerjEKgAZ5MPGZX9TkQFBxW70Xf1hExD7cuXwJujbKVmjU7OMjFWfPu7TrrIlG6SrEOHe7--PgqmITPHjB0-wQcUmY6_UFZnMnLiievB2a2VybN3_wRxRilKG2uQch45zYc6799VttsI67EO-gPWgjB9PezI_BqKiOQomR_7GWr9gilcHlQmAYdMsV4c98tJ_0P-ZbLNDk3jLtxMqImCEgaW_YeQgUck5BqFjR3774FbdkWJMCs-w3j7KtkkJN4yCFZpS7qn9d0VF7OXPEPHNYYLKeoM4q9jI8_az31vLRhM_oBagul=w701-h383-no)

## 4.2 Start Collaboration

After installation complete, a new feature appeared in VSCode

Click on that Live Share feature, then `Start collaboration session...`

![start collaboration session](https://lh3.googleusercontent.com/xsctwS3GAoe0nTciAGsYE5aYQE2sJq1Llq8YLukCJEMOU3LTiUXNxl7k2rao1d13MG5R7yQmQD4fpLGyLUM3vngH31TSobcA7yhh2raKIcXJDeFaaP3z3NZg8eTxe0nFr__AeriaZ2-3ULpPN7TKjd16AXgNe9px0M60uzyFR7iaGS6sGRsqVYZaVNdugMVzwjhsM-VmAFKFtohzxDn-wbjdqQyf9T-MmKE4Ze4Du-3K5uiQxblBOyvWiSelVXSnw4jvTZ8mu5L5LczGT4kwWGQ0aYFZ_wOAWtejpTk5Beek68vG5Km2eg-c2JK8zsOYN8EVxS4etwMtxTJ2b5wUCfhOl8ra_KC21AHqm5rHsMWM4QmKVkUjg6RneXLclNkQ1RcA3ntmInQcb3NRtLmEpA0-K58i25VrqPsTBWlpIfKarXbnSTRkpeu8IzOwBjqFLxJZWZuBLt4FhBS8Iln8f7EgZxgTynm9UudikU2B_gcwRBUebfXcFE9Y5g07hs7uhIz4ZddLU_eX7_Tpe4H0sGYgyxzjlWyb6sYODGEUQtTEE4VVzLwRA4TSoa6vef7Ek2jaUauOsbDzdT9niTydPp_AYPhZIbwn-8pQnqwfTx-5D5CJuAE4nvvFzCQJwTloIWfp9FyhUrziJztUaRTf8sJXX8pZv8BcgYxSgCqYVNFXD7HSDgmCJ-brXg1zkrPMKSRZSqzTAnz58tbV31IYw5g8=w656-h599-no)

It will open a new website that require you login with either Microsoft Account (outlook, hotmail, live) or GitHub Account.

For this tutorial, I will use my github account

![github](https://lh3.googleusercontent.com/mC6wby4g6KGGad9dFmNa9UeNer-lVYEn3QEEXqe16I-0IxBoRfnRs6T2sWt3rs0btagDKi1lgbXTKbiPOcqjTmR-_OiScKg6jp87kzVKq7RDTaZ_nd7-YGNVSnCQyl7W3HhVKJvpAcdXPpo5tMuKszkeM0kHHPnXzhNkOBTiGg3l4DyzM1w9CeIhydmwErvzgLzVfOJmosEsVPrwT8d-QT5RF9ZX01VyWmaaTcxZ725rB8iSBiAF4-T6RvwiHJB-vuSmqnioFNGjQ0llR79OfEupHrm2mPZQRqg5vGjfLTrYfP2CKJw0Qefrz_wyhFgPqJ6uMhlSnjxUY6NYZ2GQeTsdS_E4ZDm0isBFlqkd3CEJEG1WAr41ooNHPdAvH3KeeBxW9c4-BKFYubjyrodHJf5f4ub0kvhvk9Q1QqSvKftNNJhYfbXnkk_0t_sZAC5MZKgapuuXLapP0WfCv-pNP_HXXjYq4x55rCa8IBQe4c1JBFd3w6fBzULBLqCbvkfoxzXeCp039GJsqdggW4a3R2g1liyemGqmz_mgFvUYmszKM2cWesSv4HQJ4mKO1z26Rtaglj9F9POHJtNQJl55ByRvIffhJBmO_oHw8vkD_6FX1PYiY9kI4rKFg9JFsFwBDe_X3hoajxFUc4o-bsfiMztQd_LYn19Kd1DIg9Ci5p8jfIX4ECEG4u4scLO87LqA-88TzY-qkPSmsIX9bMLzcxAW=w676-h604-no)

After authorized, Live Share will start working. You can paste the generated link for other users

![copy the link](https://lh3.googleusercontent.com/WTCm3ZmcTIpKgebl1Hj6ktgKOyZVLUZa6tIAjZYK01AR0id4u2vIdbND2V7Yd6osWNFgClXDSbinESXDWVi3HT5qIIbsPJCaof6GYU9stanOWLb5LGfWD1Kwy8cqnj-q1DzBmA8UCEWgzsK-AYyA4xpl4ybhU2BEyNiS-yQKA4Jay2xXqAnFqaX4wmBPlwEePBFtJikIgiCDzPw75qKx0imDe8z9qqpADaM32cTokrXphiMM5P1tqK8yc-b4ITLd7EGkZpFuQ5QoLOVxOldmbMBmdxtoPuzJNvWBNC6KcPn_Cz8L3FwFVuw4o44jlOg2MJQh4E8FsDszh-3G5Q-9AxoiyDCvLSZMtOHYDqxyc8ApCZaVZy9CqBkDsaL627RIoUvQXE6Dgvr72O3_NDV6FfVxaHPZ1UnRtr5fqqeYrDrPRGQeUIxxfhpz7DFCy8hCuoB-USuKLUAJff3XkhEb6G35hV2jWeNaiQ3fMTikrn76gLqoU6cGZcdTRj0vT_1yHCInaB--ethRevpjISoCX8Dk6YxqY7OBk1kXM-RIO74GbMiWFhcrqkh6ul9kQMEw0RXOT60hd8ThCQtdfy3Q7gokH8bLEYHoOtXaGoBc3yhdBYMkT_nwvL3RYS2to0LBNGQqGJ6R_afekBr9gnkqKCeWUhnfg3XwVOzwLGglDYMqYQ1wERV17mNDvoAvKtps8N9HBIoGgNTmmuli1EYhAppY=w531-h435-no)

## 4.3 Join a shared collaboration session

If you are not the one who sharing, but the one who join, it's even easier.

Open Live Share feature > `Join collaboration session` > Paste the link you have to the box appeared then press `Enter`

If successful, it should be like this

![join collaboration session](https://lh3.googleusercontent.com/lLtsGd3A741aHZVSpLIIJHvN4Z6Nd0j5G4osNktOxr2K0aB0U_UPUS-C3zs0py-mt9b5psaMIbGeiaXxdO6Z-zvvRDuFRwT2O018uXGX06UIGknCKgEvCEdJypiBrVr9tUGYvc8ndiFlB6QzsScQpxuQdKAhZ-o7vEnkwSYnHrSGvFKAKjWBkMJdr8ixn6T0Cm7_qL7tsq0dNiTdUatlqPN1fP2xFNZBSUCaHjujiz5EJxyoTqMMgJAEJ_Y746I3u566vsXQYkumdbHwTWdwivO4l9NSZW52Ux1OnCPpVMyK51AvvfB3Nr7-A-cRXlWXLG1QeHt5yh0ieW3xuHXGtcvsv6iKEtC9Llm9Foczd9e1kiIDQ2rBo5KluLQmTI_aP5fM9bjQFz7CP2gjDlqET-K-kUpxj-OuA6oRE_NJ-sVEIKf526sP7pxkusS97OsF-b_G6nJd7ncbpD-3POuDHoxaUNlPMRiJ9AaHoeGMBSE_zTnmSiN3zPw63Lo49YCPTxVpWRf9FUQsHlJL0XfwGOVDHHwkJcxhzbDPvlBCWfJ_Xhryn6QGBiFm-zm4nRWch_79rw5SWvmFPXkPHIaKxt1Cn2cD-Q8tPG5M3cy9HPVpjXSuQUuxDbNbtypjfbss_tYMVTvVwpcY2VX2whYpNniHoGzDfSt_0b-aa2Xz4wu20Sf7YvyFCQssGkKntXnHGs9PeVObQUg-Po1AgQvcueqa=w956-h595-no)

## 4.4 Live Share Maximum collaborators

The short answer: 5

For more information on when/how you can increase this number can be found here: [https://github.com/MicrosoftDocs/live-share/releases/tag/0.3.788](https://github.com/MicrosoftDocs/live-share/releases/tag/0.3.788)