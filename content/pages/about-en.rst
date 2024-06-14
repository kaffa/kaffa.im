About Me
############################

:date: 1987-02-11 12:00
:modified: 2024-02-22 12:00
:slug: about
:author: Kaffa
:summary: About Me
:lang: en
:image: /static/img/2023/hero.png

.. raw:: html

    <style>
    a, a:visited, a:hover {
        color: #000;
        padding-bottom: 1px;
        margin-bottom: -1px;
        border-bottom: dotted 1px #999;
    }
    h1 a, h1 a:visited, h1 a:hover {
        border-bottom: none;
    }
    </style>
    <script src="http://kaffa.im/static/js/jquery-3.7.1.min.js"></script>
    <script>
        $(function() {
            const span = $('.spn_about');
            const div = $('.navbar-link:contains("关于")');
            const bgColor = div.css('backgroundColor');

            let flashCount = 0;
            span.on('mouseover', flash);

            function flash() {
                if (flashCount >= 10) {
                    div.css('backgroundColor', bgColor);
                    span.off('mouseover', flash);
                    return;
                }

                let opacity = flashCount / 10;
                div.css('backgroundColor', `rgba(255, 0, 0, ${opacity})`);
                flashCount++;
                setTimeout(flash, 200);
            }
        });
    </script>

No way! No way! You can’t really finally find my personal website!
================================================================================

您好, Hello!

I am the webmaster of Kaffa.im, using the nickname Kaffa. (Observer A: This sentence contains a repetition; Observer B: Hmm, it doesn't adhere to the DRY principle.)

.. raw:: html

   <p>As you can see, I am in China, where I use Chinese in my daily life and also understand some English. I hope language will not be a barrier for communication between people. With this wish in mind, on one hand, I hope friends who do not speak Chinese, no matter where you are from, can learn Chinese; on the other hand, I am honored that you are here, and you are always welcome to contact me through the <span class="spn_about">"About"</span> menu. Alternatively, if you are familiar with Feed/RSS/Atom, you can subscribe to my content updates through the <a href="https://kaffa.im/feeds/all.atom.xml">"Subscribe to Feed"</a> option, which is likely a faster way to get my content updates.</p>

Perhaps you are familiar with the Latin language and know the word "kaffa," or perhaps coincidentally, something clever happens—you come from or have been to Kaffa Province, Ethiopia!

In 2018, I chose to use this nickname because I am a fan of `third wave coffee <https://kaffa.im/specialty-coffee-science-volume-1.html>`_. Legend has it that coffee was discovered by shepherds in the Kaffa Forest. If given the opportunity, I would love to visit the birthplace of Arabica beans to trace their origins and taste truly fresh Typica and Bourbon.

Initially, I gave the word "Kaffa" the meaning of Keep Agile & Free. However, now in 2023, I have upgraded my website and given it `a new meaning <https://kaffa.im/on-kaffa-im-new-website.html>`_.


What content is available here?
========================================

To be completely honest, there is no business involved here! Affiliate links will be clearly marked as AFF, with the main purpose being to make friends with you.

For your convenience in understanding this site, I have added a page of explanation, which can be found under the menu `About - Website <https://kaffa.im/pages/about-website.html>`_ .

Who am I?
====================

"If you're in a hurry, then the answer is in the concluding sentences of this section. The following paragraphs are a little bit of reflection."

The management guru tells us, "Don't let your job define you." But frankly, for most of the poor working people living in the 21st century, work is not something "elsewhere"; your job is almost you. The guru's assertion should perhaps be replaced with "Don't let your title define you," as titles are akin to labels, representing a role or identity.

Perhaps within your field, your position may be at the top or middle management level, but those are not who you are. Your industry and the work your company does are closer to the real you. As for who you want to be or what you want to do, those are not you (one-liner flashes), they are just your consciousness setting up a "SUPER YOU" to escape the present and simulate for the future.

Undoubtedly, most of me or us are closer to the work we have been engaged in for many years.

In over twenty years of software development, what has changed are the titles and positions, while what remains constant is my continuous provision of software selection, usage, and advice to those in need, as well as my dedication to helping service providers and clients solve software difficulties and uncertainties. Meanwhile, I also engage in custom development for those with specific software requirements. As the industry evolves, I have found myself using over 20 programming languages, working on all mainstream operating systems, leading teams of various sizes, and developing software in various forms ranging from desktop to web to AI. I believe that a significant portion of the code I have written will continue to work persistently, contributing to both "ancient" and modern businesses.

Unlike the choices made by the companies I work for (most of which tend to opt for more expensive solutions, often from Fortune 500 companies [#f1]_), my software development process is based on real customer scenarios. It involves selecting and customizing cost-effective solutions according to the actual needs and context of the customer. Furthermore, I am committed to providing equivalent, secure, and reliable products and services without compromising on functionality and features. I also aim to provide ongoing consultancy and create value for customers in a more sustainable manner.

"It sounds quite complicated!"

Simply put, I develop software and I'm good at it. Besides that, I'm also a coffee enthusiast, three cats parent, a lifelong learner, enjoy reading books, photography, and tinkering with software."


Identity and Real Name
========================================

.. image:: https://kaffa.im/static/img/2023/internet-dog.jpg
    :alt: Internet Dog

"On the Internet, nobody knows you're a dog." —— Peter Steiner

Cartoonist Peter Steiner has also written many novels throughout his life. In the end, whether it's the traces of history or the creations of humans, identity is the fictitious mask of people.

A master named Qian once said: "If you love her, read her code. When you eat an egg, you don't have to think about looking at the chicken that laid it."

Master Qian is telling us that without identity and real names, it is easier to get to know you in interaction.

More often than not, as creators of bytes on the internet, we cannot be like Eileen Chang, who wrote "`Half a Lifelong Romance`_" and then produced "`Little Reunions`_"; we cannot be like `RMS`_, who wrote `Emacs`_ and then released `GCC`_; we cannot be like `Linus Torvalds`_, who contributed to `Linux`_ and then created `Git`_; nor can we be like `Yao Zhongren`_, who wrote "Shockwave baseball" and "Mr. Almost", maintaining his influence even in old age, and then released "The Dirty Artist".

And if the times, if the times do not choose us, like most of the almost-missed gentlemen and ladies of this era, we will code in the public domain, while leaving behind some local, simple bytes. That's what I kreated\ [#f2]_ for the world.

Personal Website
====================

As a survivor of the PC era, I am also a webmaster, one who had a personal homepage in the early days of the Chinese internet. I used Netscape Navigator distributed on CDs, looked up CET-4 and CET-6 exams result on etang.com, created a homepage on yeah.net provided by NetEase, and searched for alumni records on ChinaRen.com. I also experienced the blogging era of Web 2.0 and the app era of mobile internet, during which high-quality Chinese content gradually moved into private domains and mini-apps.

People now understand that attention is a limited resource, which is less than or equal to the total sum of everyone's autonomous time (including leisure time). Fewer people are willing to use independent domains to continuously publish content.

This site chooses to use an independent domain, which aligns more closely with its purpose and reflects independent thinking. However, it should also be noted that independence is relative. While we gain independence from our primitive biological state and gain a sense of empowerment, we also sever connections with others, which is always a contradiction.

Therefore, I often connect with experts in various fields, such as Jeremy Thomas and Justin Mayer. In my work, I have often benefited from these generous sharers. Perhaps I don't possess the technical depth of top experts in the field, but with the help of what these sharers provide, I have created several versions of websites. I'm neither a genius nor an expert; I'm just standing on the shoulders of these sharers.

In this best of times and worst of times, in this era of cognitive surplus and overwhelmed nerves, I hope to use my free time to engage in more creative activities, with Kaffa.im serving as a gathering place for online life.

"This website is personal"
========================================

"This website is personal" means "\ `This website is personal <https://kaffa.im/this-website-is-personal.html>`_\ ", which is part of a "small web" movement in 2021. To put it bluntly, it is to achieve that personal content is controlled by individuals, rather than being "handled" and decided by giant companies and platforms.

This requires us to proactively post all personal content on our personal websites and only post links to the original content on social media.

The benefit of publishing content to a place where you can control it is that you can control the content. These places include but are not limited to home servers and cloud infrastructures. Use open source content publishing tools for content publishing, and then publish the recent activities of content publishing to social media, In this way, when people visit the content you create, they will eventually link to your website. Of course, you can also copy and publish it, but you can use some publishing chains and publishing timelines to ensure the originality of the content.

There is a problem that needs to be solved here. The replies and discussions of your friends and fans on social media need to be centralized back to your website in some simple way. The Internet Standards Organization has discussed similar standards called webmention and microformat. You can search for open source implementations to achieve this goal through these two keywords.

Records on My Exploration of the World
========================================

Based on human ego's partial self-awareness and the elephant's willful blindness to the rider in the circus, I identify more with being a "`Random Walker`_" in life.

I consider myself fortunate to have experienced a fairly complete Kondratiev long wave cycle in my life, and I'm also lucky that my profession has given me the ability to independently build websites. As this "fool" stands at the cusp of destiny, I can also use this platform to record my exploration and enjoyment of the constantly changing " **Winds** ."

Finally, if you've managed to read this far, it's a rarity. I have no gift to offer, but borrowing a sketch from Zhang Zongzi, let us enjoy it together:

    Viewing Snow from the Pavilion on the Lake [Ming Dynasty] by Zhang Dai, from "`Dreams of the Tao An Retreat <https://kaffa.im/tao-an-meng-yi.html>`_".

    In the twelfth month of the fifth year of the Chongzhen Era, I resided by West Lake. It snowed heavily for three days, and all sounds of people and birds on the lake ceased. On that day, I made up my mind and took a small boat, wrapped in fur clothes with a stove, and went alone to the Pavilion on the Lake to view the snow. The mist and snow merged together, and the sky, clouds, mountains, and water all turned white. The only trace on the lake was the long embankment, the Pavilion on the Lake, and my boat, all appearing like tiny specks. Inside the boat, there were only two or three people.

    Upon arriving at the pavilion, I saw two people sitting opposite each other on a felt mat, with a young servant boy boiling wine on the stove. Seeing me, they expressed great surprise and said, "Where else could there be someone on the lake today?" They invited me to drink with them. I reluctantly drank three cups of wine and then left. I asked for their surnames; they were from Jinling and were just visiting here. As I departed from the boat, the boatman muttered, "Don't say that the gentleman is idealistic; there is someone even more idealistic than the gentleman."


Logs
--------------------

2024-01-05

- Added the section "Who am I";
- Included links to books and software.

2024-02-22

- Wasn't satisfied with the writing style, made a lot of edits, resulting in a significant increase in word count, felt the readability improved.

2024-03-03

- Added an English version.

Footnotes
====================

.. [#f1] Many large companies do not operate on a lowest-cost strategy but instead utilize appropriate competitive strategies to develop products and services, capture market share, and compete with rivals. For example, they leverage their size to gain bargaining power, reduce marketing costs through existing channels, attract top talent, limit access to talent for competitors, and outsource services to transfer labor costs. However, the tactics used by large companies would essentially render small companies unable to compete if replicated.

.. [#f2] kreate = create. A personal original English term, similar examples include "kunnect" for "connect".


.. _`Little Reunions`: https://kaffa.im/little-reunions.html
.. _`Half a Lifelong Romance`: https://kaffa.im/half-a-lifelong-romance.html
.. _`Random Walker`: https://kaffa.im/fooled-by-randomness.html
.. _RMS: https://stallman.org/
.. _Emacs: https://kaffa.im/emacs.html
.. _GCC: https://gcc.gnu.org/
.. _`Linus Torvalds`: https://github.com/torvalds
.. _`Linux`: https://www.linux.org/
.. _`Git`: https://git-scm.com/
.. _`Yao Zhongren`: https://www.google.com/search?q=%E5%A7%9A%E4%B8%AD%E4%BB%81
