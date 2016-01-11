nodewatcher: A substrate for growing your own community network
===============================================================

*nodewatcher* is one of the projects of `wlan slovenija`_ open wireless
network. Its main goal is the `development`_ of an open source network planning,
deployment, monitoring and maintanance platform with emphasis on community.

.. _wlan slovenija: https://wlan-si.net
.. _development: https://dev.wlan-si.net/wiki/Nodewatcher

This repository contains a paper presenting the project. The paper was published in
journal `Computer Networks`_, in the `special issue on community networks`_,
`DOI 10.1016/j.comnet.2015.09.021`_.

.. _Computer Networks: http://www.journals.elsevier.com/computer-networks
.. _special issue on community networks: http://www.sciencedirect.com/science/journal/13891286/93/supp/P2
.. _DOI 10.1016/j.comnet.2015.09.021: http://dx.doi.org/10.1016/j.comnet.2015.09.021

You can cite it as::

    @article{Kos2015279,
      title = "nodewatcher: A substrate for growing your own community network",
      journal = "Computer Networks",
      volume = "93, Part 2",
      pages = "279--296",
      year = "2015",
      issn = "1389-1286",
      doi = "http://dx.doi.org/10.1016/j.comnet.2015.09.021",
      author = "Jernej Kos and Mitar Milutinović and Luka Čehovin",
      keywords = "Community networks",
      keywords = "Management",
      keywords = "Provisioning",
      keywords = "Monitoring",
      keywords = "Wireless",
      keywords = "Mesh"
    }

Abstract:

    Community networks differ from regular networks by their organic growth patterns — there is no central planning
    body that would decide how the network is built. Instead, the network grows in a bottom-up fashion as more people
    express interest in participating in the community and connect with their neighbors. People who participate in
    community networks are usually volunteers with limited free time. Due to these factors, making the management of
    community networks simpler and easier for all participants is the key component in boosting their growth.
    Specifics of individual networks often force communities to develop their own sets of tools and best practices
    which are hard to share and do not interoperate well with others. We propose a new general community network
    management platform *nodewatcher* that is built around the core principle of modularity and extensibility, making
    it suitable for reuse by different community networks. Devices are configured using a platform-independent
    configuration which *nodewatcher* can transform into deployable firmware images, eliminating any manual device
    configuration, reducing errors, and enabling participation of novice maintainers. An embedded monitoring system
    enables live overview and validation of the whole community network. We show how the system successfully operates
    in an actual community wireless network, *wlan slovenija*.
