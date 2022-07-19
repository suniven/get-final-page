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