CREATE TABLE IF NOT EXISTS `round_1`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page`     varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page url',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page url',
    `status_code`      varchar(3)                NOT NULL DEFAULT '' COMMENT '响应状态码',
    `a_num`            int                       NOT NULL DEFAULT 0 COMMENT 'number of a tags found in landing page',
    `vpn`              varchar(20)               NOT NULL DEFAULT '' COMMENT 'vpn',
    `checked`          varchar(50)               NOT NULL DEFAULT '' COMMENT '人工分类结果',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='round_1';


CREATE TABLE IF NOT EXISTS `round_2`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page_1`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_1',
    `landing_page_2`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_2',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page 2 url',
    `a_num`            int                       NOT NULL DEFAULT 0 COMMENT 'number of a tags found in landing page 2',
    `vpn`              varchar(20)               NOT NULL DEFAULT '' COMMENT 'vpn',
    `checked`          varchar(50)               NOT NULL DEFAULT '' COMMENT '人工分类结果',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='round_2';

CREATE TABLE IF NOT EXISTS `round_3`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page_1`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_1',
    `landing_page_2`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_2',
    `landing_page_3`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_3',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page 2 url',
    `a_num`            int                       NOT NULL DEFAULT 0 COMMENT 'number of a tags found in landing page 3',
    `vpn`              varchar(20)               NOT NULL DEFAULT '' COMMENT 'vpn',
    `checked`          varchar(50)               NOT NULL DEFAULT '' COMMENT '人工分类结果',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='round_3';


CREATE TABLE IF NOT EXISTS `final_page`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page`     varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page url',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page url',
    `domain`           varchar(50)               NOT NULL DEFAULT '' COMMENT 'domain',
    `a_num`            int                       NOT NULL DEFAULT 0 COMMENT 'a标签的数量',
    `vpn`              varchar(20)               NOT NULL DEFAULT '' COMMENT 'vpn',
    `type`             varchar(100)              NOT NULL DEFAULT '' COMMENT '网站类型',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='final page';


CREATE TABLE IF NOT EXISTS `html`
(
    `id`           bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`          varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page` varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page',
    `html`         mediumtext                NOT NULL COMMENT 'html',
    `create_time`  bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='html';


ALTER TABLE html
    CHANGE html html mediumtext CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS `html_middle`
(
    `id`           bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`          varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page` varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page',
    `html`         mediumtext                NOT NULL COMMENT 'html',
    `create_time`  bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='html_middle';

ALTER TABLE html_middle
    CHANGE html html mediumtext CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS `example`
(
    `id`           bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`          varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page` varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page',
    `a_count`      int                       NOT NULL DEFAULT 0 COMMENT 'a标签数量',
    `img_count`    int                       NOT NULL DEFAULT 0 COMMENT 'img标签数量',
    `iframe_count` int                       NOT NULL DEFAULT 0 COMMENT 'iframe数量',
    `button_count` int                       NOT NULL DEFAULT 0 COMMENT 'button数量',
    `div_count`    int                       NOT NULL DEFAULT 0 COMMENT 'div数量',
    `class_count`  int                       NOT NULL DEFAULT 0 COMMENT 'class种类',
    `words_count`  int                       NOT NULL DEFAULT 0 COMMENT '网页字符数',
    `js_count`     int                       NOT NULL DEFAULT 0 COMMENT 'js数量',
    `link_count`   int                       NOT NULL DEFAULT 0 COMMENT 'link标签数量',
    `a_http`       float                     NOT NULL DEFAULT 0 COMMENT 'a href 使用 http 比例',
    `a_https`      float                     NOT NULL DEFAULT 0 COMMENT 'a href 使用 https 比例',
    `link_http`    float                     NOT NULL DEFAULT 0 COMMENT 'link http',
    `link_https`   float                     NOT NULL DEFAULT 0 COMMENT 'link https',
    `a_diff`       float                     NOT NULL DEFAULT 0 COMMENT 'href链接与原URL域名不同的数量占比',
    `link_diff`    float                     NOT NULL DEFAULT 0 COMMENT 'href链接与原URL域名不同的数量占比',
    `a_hashtag`    float                     NOT NULL DEFAULT 0 COMMENT 'href=# or jsvoid0',
    `link_hashtag` float                     NOT NULL DEFAULT 0 COMMENT '同上',
    `tag`          int                       NOT NULL DEFAULT 0 COMMENT '0-middle 1-final',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='example';