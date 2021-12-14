<template>
    <q-scroll-area :thumb-style="thumbStyle"
                   :bar-style="barStyle"
                   :visible="visible"
                   ref="scrollAreaIndex"
                   @scroll="onScroll()"
                   :style="{ height: scroll_height, width: scroll_width }"
    >
      <q-layout view="lHh Lpr lff" ref="Index">
          <q-header>
            <div class="row" style="height:110px">
              <div class="col-2"></div>
              <div class="col-2" style="align-self: center">
                <q-btn
                  icon="img:statics/logo.svg"
                  round
                  dense
                  unelevated
                  flat
                  to="/"
                />
                <a href="/" style="color: white; text-decoration:none">
                  {{ $t('index.title') }}
                </a>
                </div>
              <div class="col-6" style="align-self: center">
                <q-btn-group flat >
                  <q-btn flat :label=navbar.front_page to="/"></q-btn>
                  <q-btn flat :label=navbar.community to="/bbs"></q-btn>
                  <q-btn flat :label=navbar.market></q-btn>
                  <q-btn-dropdown flat :label=navbar.demo>
                    <q-list>
                      <q-item clickable v-close-popup @click="goTo('http://www.quasarchs.com/vue-components/button/')">
                        <q-item-section>
                          <q-item-label>IOS</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item clickable v-close-popup @click="goTo('http://www.quasarchs.com/vue-components/button/')">
                        <q-item-section>
                          <q-item-label>Android</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item clickable v-close-popup @click="goTo('http://www.quasarchs.com/vue-components/button/')">
                        <q-item-section>
                          <q-item-label>Ipad</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item clickable v-close-popup @click="goTo('http://www.quasarchs.com/vue-components/button/')">
                        <q-item-section>
                          <q-item-label>Windows</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-btn-dropdown>
                  <q-btn
                    :label=navbar.contact
                    @click="contact = true"
                  />
                  <!--          选择语言下拉框-->
                  <q-btn-dropdown :label=langlable>
                    <q-list>
                      <q-item clickable v-close-popup @click="langChange('zh-hans')">
                        <q-item-section>
                          <q-item-label>{{ $t('index.lang.zh_zhans') }}</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item clickable v-close-popup @click="langChange('en-US')">
                        <q-item-section>
                          <q-item-label>{{ $t('index.lang.English') }}</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item clickable v-close-popup @click="langChange('ja')">
                        <q-item-section>
                          <q-item-label>{{ $t('index.lang.ja') }}</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item clickable v-close-popup @click="langChange('zh-hant')">
                        <q-item-section>
                          <q-item-label>{{ $t('index.lang.zh_zhant') }}</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-btn-dropdown>
                </q-btn-group>
              </div>
              <div class="col-2"></div>
            </div>
          </q-header>
        <q-separator inset />
        <q-page-container>
          <q-page>
            <div class="column" style="height: 3529px">
<!--              第一个模块-->
              <div class="col">
                <div style="position: relative">
                  <svg width="100%" height="100%" viewBox="0 0 1920 880" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                    <g id="页面-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <g id="首页" fill="#1370EE">
                        <path d="M0,0 L1920,0 L1920,599.84668 C1920,651.063565 1881.30299,694.001406 1830.3618,699.308397 L110.3618,878.495887 C55.4306103,884.218551 6.26094715,844.32716 0.538283207,789.39597 C0.179669518,785.953679 -3.75978507e-14,782.495091 0,779.034171 L0,0 L0,0 Z" id="矩形"></path>
                      </g>
                    </g>
                  </svg>
                  <div style="position:absolute;left:31%; top:10%;font-size: 60px;font-weight: normal;color: white;letter-spacing: 10px;text-align: center">
                    {{ $t('index.title') }}
                    <br>
                    {{ $t('index.title2') }}
                    <br>
                    <q-btn size="xl" style="background-color:#FFCE05;width: 260px;height: 66px;margin-top: 10%" align="left" icon ="img:statics/gitee.svg"><span style="color: black;font-size: 30px;font-weight: normal;margin-left: 15%">{{ code_warehous }}</span></q-btn>
                  </div>
                  <q-img src="/statics/computer.svg" style="position: absolute;left: 19%;top:50%;width: 61%"/>
                  <q-media-player
                    type="video"
                    background-color="black"
                    :muted="muted"
                    radius="1rem"
                    :autoplay="true"
                    :show-big-play-button="true"
                    :sources="video.sources"
                    :poster="video.poster"
                    :tracks="video.tracks"
                    track-language="English"
                    @ended="onEnded"
                  >
                    <template v-slot:overlay>
                      <div>
                        <img
                          src="public/statics/logo.svg"
                          style="width:50px; max-width: 50px;"
                        >
                      </div>
                    </template>
                  </q-media-player>
                </div>
              </div>
<!--               第二个模块-->
              <div class="col" style="text-align: center;margin-bottom: -20%">
                <span style="font-size: 32px;font-weight: normal;text-align: center">{{ $t('index.features') }}</span>
                <q-separator inset style="color: #FFCE05;width: 40px;background-color:#FFCE05;margin-left: 49.1%;margin-top: 1%" />
                <div class="row" style="margin-top: 70px">
                  <div class="col-2"></div>
<!--                  第一个卡片-->
                  <div class="col-2" style="height: 270px">
                    <div class="q-pa-md aaa">
                      <q-card flat>
                        <q-item>
                          <q-item-section avatar>
                            <q-avatar square icon="img:statics/equipment1.svg" size="120px"></q-avatar>
                          </q-item-section>
                        </q-item>
                        <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                          <div style="font-size: 22px">{{ $t('avtar.tip1') }}</div>
                          <br>
                          <div style="font-size: 14px">{{ $t('avtar.tip_note1') }}</div>
                        </q-card-section>
                      </q-card>
                    </div>
                  </div>
                  <!--                  第二个卡片-->
                  <div class="col-2">
                    <div class="q-pa-md aaa">
                    <q-card flat>
                      <q-item>
                        <q-item-section avatar>
                          <q-avatar square icon="img:statics/equipment2.svg" size="120px"></q-avatar>
                        </q-item-section>
                      </q-item>
                      <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                        <div style="font-size: 22px">{{ $t('avtar.tip2') }}</div>
                        <br>
                        <div style="font-size: 14px">{{ $t('avtar.tip_note2') }}</div>
                      </q-card-section>
                    </q-card>
                  </div></div>
                  <!--                  第三个卡片-->
                  <div class="col-2">
                    <div class="q-pa-md aaa">
                    <q-card flat>
                      <q-item>
                        <q-item-section avatar>
                          <q-avatar square icon="img:statics/equipment3.svg" size="120px"></q-avatar>
                        </q-item-section>
                      </q-item>
                      <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                        <div style="font-size: 22px">{{ $t('avtar.tip3') }}</div>
                        <br>
                        <div style="font-size: 14px">{{ $t('avtar.tip_note3') }}</div>
                      </q-card-section>
                    </q-card>
                  </div></div>
                  <!--                  第四个卡片-->
                  <div class="col-2">
                    <div class="q-pa-md aaa">
                    <q-card flat>
                      <q-item>
                        <q-item-section avatar>
                          <q-avatar square icon="img:statics/equipment4.svg" size="120px"></q-avatar>
                        </q-item-section>
                      </q-item>
                      <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                        <div style="font-size: 22px">{{ $t('avtar.tip4') }}</div>
                        <br>
                        <div style="font-size: 14px">{{ $t('avtar.tip_note4') }}</div>
                      </q-card-section>
                    </q-card>
                  </div></div>
                  <div class="col-2"></div>
                </div>
              </div>
<!--              第三个模块-->
              <div class="col" style=" margin-top: -10%;margin-bottom: -13%">
                <div style="position: relative">
                  <svg width="100%" height="100%" viewBox="0 0 1920 765" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

                    <g id="页面-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <g id="首页-软件演示" transform="translate(0.000000, -1658.000000)" fill="#F6F6F8">
                        <path d="M0,1649 L1920,1649 L1920,2157.6964 C1920,2209.42844 1880.54416,2252.62062 1829.02315,2257.28848 L109.023153,2413.12238 C54.0199647,2418.10573 5.39126796,2377.55664 0.407918399,2322.55345 C0.136111606,2319.55341 -2.80528059e-14,2316.54263 0,2313.5303 L0,1649 L0,1649 Z" id="矩形备份-2" transform="translate(960.000000, 2036.000000) scale(-1, -1) translate(-960.000000, -2036.000000) "></path>
                      </g>
                    </g>
                  </svg>
<!--                  左侧图-->
                  <q-img src="/statics/computer2.svg" style="position: absolute;left: 15.31%;top:4%;width: 30%"/>
<!--                  右侧文字-->
                  <div class="column" style="position: absolute;left: 54%;top:23%">
                   <span class="col-3" style="font-size: 32px;font-weight: 500">
                     {{ $t('avatar2.tit') }}
                     <br>
                    <q-separator inset style="color: #FFCE05;width: 40px;background-color:#FFCE05;margin-left: -0.1%;margin-top: 3%" />
                    <br>
                   </span>
<!--                    01-->

                      <div class="col-3" style="margin-bottom: 3% ">
                        <span  style="font-weight: bold;color: #999999;font-size: 22px;">
                           01
                        </span>
                        <span style="font-size: 18px;font-weight: 500;margin-left: 5%;color: #333333">
                        {{ $t('avatar2.tip1') }}
                      </span>
                        <br>
                        <span style="width: 50.2%;float: left !important; overflow: hidden !important; text-overflow: ellipsis !important; white-space: normal !important;margin-left: 8.5%;font-size: 14px;font-weight: 400;color: #666666;line-height: 21px;
letter-spacing: 2px;margin-top: 2%">
                          {{ $t('avatar2.tip1_note') }}
                        </span>
                      </div>
<!--                    02-->
                    <div class="col-3" style="margin-bottom: 1% ">
                        <span  style="font-weight: bold;color: #999999;font-size: 22px;">
                           02
                        </span>
                      <span style="font-size: 18px;font-weight: 500;margin-left: 5%;color: #333333">
                        {{ $t('avatar2.tip2') }}
                      </span>
                      <br>
                      <span style="width: 50.2%;float: left !important; overflow: hidden !important; text-overflow: ellipsis !important; white-space: normal !important;margin-left: 8.5%;font-size: 14px;font-weight: 400;color: #666666;line-height: 21px;
letter-spacing: 2px;;margin-top: 2%">
                          {{ $t('avatar2.tip2_note') }}
                        </span>
                    </div>
<!--                    03-->
                    <div class="col-3" style="margin-bottom: 5% ">
                        <span  style="font-weight: bold;color: #999999;font-size: 22px;">
                           03
                        </span>
                      <span style="font-size: 18px;font-weight: 500;margin-left: 5%;color: #333333">
                        {{ $t('avatar2.tip3') }}
                      </span>
                      <br>
                      <span style="width: 50.2%;float: left !important; overflow: hidden !important; text-overflow: ellipsis !important; white-space: normal !important;margin-left: 8.5%;font-size: 14px;font-weight: 400;color: #666666;line-height: 21px;
letter-spacing: 2px;;margin-top: 2%">
                          {{ $t('avatar2.tip3_note') }}
                        </span>
                    </div>
                  </div>
                </div>
              </div>
<!--              第四个模块-->
              <div class="col">
                <div style="position: relative;text-align: center">
                  <span style="font-size: 32px;font-weight: 500;letter-spacing: 4px;color: #333333;margin-bottom: 20%">{{ $t('avatar3.awards') }}</span>
                  <q-separator inset style="color: #FFCE05;width: 40px;background-color:#FFCE05;margin-left: 49.1%;margin-top: 1%" />
<!--                  背景图-->
                  <q-img src="statics/map.png" style="width: 100%;height: 100%;margin-top: 5%"/>
                    <q-img src="statics/award.png" style="width: 27%;position: absolute;left: 17%;top: 61%"/>
                  <div style="position: absolute;left: 54%;top: 63%">
                    <span style="width: 60%;font-size: 22px;font-weight: 500;text-align: left;color: #ffffff;line-height: 33px;letter-spacing: 1px;float: left !important; overflow: hidden !important; text-overflow: ellipsis !important; ">
                      {{ $t('avatar3.tip_note') }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
<!--            回到顶部-->
            <q-page-sticky v-show='pagelocation > 0.5' position="bottom-right" :offset="[18, 18]" @click="ScrollToTop()">
              <q-fab
                icon="arrow_upward"
                color="primary"
            >
            </q-fab>
          </q-page-sticky>
          </q-page>
          </q-page-container>
<!--        页脚-->
        <q-footer>
          <div class="row" style="height: 300px">
            <div class="col-2"></div>
            <div class="col-2">
              <q-img src="statics/logo_under.svg" width="6%"/>
              <span style="width: 118px;height: 22px;font-size: 20px;font-weight: 700;text-align: left;color: #000000;line-height: 22px;">{{ $t('index.title') }}</span>
            </div>
            <div class="col-2"></div>
            <div class="col-4"></div>
            <div class="col-2"></div>
          </div>
        </q-footer>
        <q-dialog v-model="contact">
            <q-card style="width: 680px!important;height: 498px; overflow-x: hidden">
              <q-bar style="height: 70px;background-color:white;">
                  <span style="font-size: 24px;font-weight: bold;color: black;margin-left: 43%;                                                                                                                               ">{{ $t('index.navbar.contact') }}</span>
                <q-space/>
                <q-btn round dense flat icon="close" v-close-popup />
              </q-bar>
               <q-separator inset />
              <q-card class="my-card" flat>
                <q-card-section horizontal>
      <!--            左侧填写框-->
                  <q-card-section style="width: 47%; margin-left: 3%">
      <!--              姓名-->
                    <div>
                      <span style="font-size: 18px">{{ $t('contactdia.name') }}</span>
                      <q-input
                        outlined
                        v-model="text"
                        style="margin-top:2%"
                      />
                    </div>
      <!--              邮箱-->
                    <div style="margin-top: 5%">
                      <span style="font-size: 18px">{{ $t('contactdia.email') }}</span>
                      <q-input
                        outlined
                        v-model="text"
                        style="margin-top:2%"
                      />
                    </div>
      <!--              企业名称-->
                    <div style="margin-top: 5%">
                      <span style="font-size: 18px">{{ $t('contactdia.company') }}</span>
                      <q-input
                        outlined
                        v-model="text"
                        style="margin-top:2%"
                      />
                    </div>
                  </q-card-section>
      <!--右侧填写框：留言-->
                  <q-card-section>
                    <div class="q-pa-md" style="width: 153%;margin-left: -10%;margin-top: -4.5%;height: 100%">
                      <span style="font-size: 18px;">{{ $t('contactdia.message') }}</span>
                      <textarea
                        v-model="text"
                        type="textarea"
                        autocapitalize="sentences"
                        maxlength="200"
                        style="width: 100%; height: 100%; resize: none"
                      />
                    </div>
                  </q-card-section>
                </q-card-section>
                  <q-btn color="#FFFFFF" style="width: 91.17%;background-color:#1370EE;font-size: 20px;margin-left: 4.3%">
                    <div class="ellipsis">
                      {{ $t('index.submit') }}
                    </div>
                  </q-btn>
              </q-card>
            </q-card>
        </q-dialog>
      </q-layout>
    </q-scroll-area>
</template>
<style lang="scss" scoped>
textarea:focus {
    outline: none;
    border-color: blue;
    box-shadow: 0 0 5px blue;
}
//.row div{
//  padding: 10px 15px;
//  background: rgba(86,61,124,.15);
//  border: 1px solid rgba(86,61,124,.2)
//}
//
//.row + .row{
//  margin-top: 1rem
//}
.aaa:hover {
  //background-position: right center;
  //box-shadow: 0 12px 20px -11px #5b86e5;
  background: #ffffff;
  border-radius: 26px;
  box-shadow: 0px 10px 30px 9px rgba(192,192,192,0.10);
  transition: all 0.3s ease-in-out;
}
.aaa {
  width: 90%;
}
</style>
<script>
import { defineComponent, ref } from 'vue'
import { openURL, createMetaMixin, Screen, LocalStorage } from 'quasar'

export default defineComponent({
  name: 'Index',
  data () {
    return {
      title: '',
      meta: {},
      lang: this.$i18n.locale,
      langlable: '',
      contact: false,
      navbar: {
        front_page: this.$t('index.navbar.frontpage'),
        community: this.$t('index.navbar.community'),
        market: this.$t('index.navbar.market'),
        demo: this.$t('index.navbar.demo'),
        contact: this.$t('index.navbar.contact')
      },
      visible: false,
      scroll_width:  Screen.width + '' + 'px',
      scroll_height: Screen.height + '' + 'px',
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#E0E0E0',
        width: '8px',
        opacity: 0.75
      },
      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#EEEEEE',
        width: '12px',
        opacity: 0.2
      },
      pagelocation: 0,
      code_warehous: this.$t('index.code_warehouse'),
      video: {
        label: 'Tears of Steel',
        poster: 'media/TearsOfSteel/TearsOfSteel.jpeg',
        sources: [
          {
            src: 'https://www.bilibili.com/video/BV177411P7d1?p=8&t=3.8',
            type: 'video/mp4'
          }
        ]
      }
    }
  },
  mixins: [
    createMetaMixin(function () {
      return {
        title: this.title,
        meta: this.meta
      }
    })
  ],
  methods: {
    goTo (e) {
      openURL(e)
    },
    langChange (e) {
      var _this = this
      _this.lang = e
      window.setTimeout(() => {
        location.reload()
      }, 1)
    },
    onScroll () {
      var _this = this
      _this.pagelocation = _this.$refs.scrollAreaIndex.getScrollPercentage().top
      console.log(_this.$refs.scrollAreaIndex.getScrollPercentage())
    }
  },
  created() {
    var _this = this
    _this.title = 'GreaterWMS - 开源社区'
    _this.meta = {
      description: {name: 'description', content: 'GreaterWMS - Open Source Warehouse Management System'},
      keywords: {name: 'keywords', content: 'Quasar website'},
      equiv: {'http-equiv': 'Content-Type', content: 'text/html; charset=UTF-8'},
      // note: for Open Graph type metadata you will need to use SSR, to ensure page is rendered by the server
      ogTitle: {
        property: 'og:title',
        // optional; similar to titleTemplate, but allows templating with other meta properties
        template(ogTitle) {
          return `${ogTitle} - GreaterWMS`
        }
      }
    }
    if (_this.lang === 'zh-hans') {
      _this.langlable = '简体中文'
    } else if (_this.lang === 'zh-hant') {
      _this.langlable = '繁體中文'
    } else if (_this.lang === 'ja') {
      _this.langlable = '日本語'
    } else if (_this.lang === 'en-US'){
      _this.langlable = 'English'
    } else {
      _this.langlable = 'English'
    }
  },
  watch: {
    lang (lang) {
      var _this = this
      LocalStorage.set('lang', lang)
      _this.$i18n.locale = lang
    }
  },
  setup () {
    const position = ref(0)
    const scrollAreaIndex = ref(null)
    return {
      position,
      scrollAreaIndex,
      ScrollToTop () {
        scrollAreaIndex.value.setScrollPosition('vertical', position.value, 100)
      }
    }
  }
})
</script>
