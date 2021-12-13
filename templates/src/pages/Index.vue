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
              <div class="col-5" style="align-self: center">
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
              <div class="col-3" style="align-self: center">
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
                  <div style="position:absolute;left:35%; top:10%;font-size: 60px;font-weight: normal;color: white;letter-spacing: 10px;text-align: center">
                    {{ $t('index.title') }}
                    <br>
                    {{ $t('index.title2') }}
                    <br>
                    <q-btn style="width: 260px;height: 66px;background-color:#FFCE05"><span style="color: black;font-size: 30px;font-weight: normal">{{ code_warehous }}</span></q-btn>
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
              <div class="col" style="text-align: center">
                <span style="font-size: 32px;font-weight: normal;text-align: center">{{ $t('index.features') }}</span>
                <q-separator inset style="color: #FFCE05;width: 40px;background-color:#FFCE05;margin-left: 49%;margin-top: 1%" />
                <div class="row" style="margin-top: 70px">
                  <div class="col-2"></div>
<!--                  第一个卡片-->
                  <div class="col-2" style="height: 270px">
                    <div class="q-pa-md">
                      <q-card flat>
                        <q-item>
                          <q-item-section avatar>
                            <q-avatar square icon="img:statics/equipment.svg" size="120px"></q-avatar>
                          </q-item-section>
                        </q-item>
                        <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                          <div style="font-size: 22px">{{ $t('avtar1.tip') }}</div>
                          <br>
                          <div style="font-size: 14px">{{ $t('avtar1.tip_note') }}</div>
                        </q-card-section>
                      </q-card>
                    </div>
                  </div>
                  <div class="col-2"><div class="q-pa-md">
                    <q-card flat>
                      <q-item>
                        <q-item-section avatar>
                          <q-avatar square icon="img:statics/equipment.svg" size="120px"></q-avatar>
                        </q-item-section>
                      </q-item>
                      <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                        <div style="font-size: 22px">{{ $t('avtar1.tip') }}</div>
                        <br>
                        <div style="font-size: 14px">{{ $t('avtar1.tip_note') }}</div>
                      </q-card-section>
                    </q-card>
                  </div></div>
                  <div class="col-2"><div class="q-pa-md">
                    <q-card flat>
                      <q-item>
                        <q-item-section avatar>
                          <q-avatar square icon="img:statics/equipment.svg" size="120px"></q-avatar>
                        </q-item-section>
                      </q-item>
                      <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                        <div style="font-size: 22px">{{ $t('avtar1.tip') }}</div>
                        <br>
                        <div style="font-size: 14px">{{ $t('avtar1.tip_note') }}</div>
                      </q-card-section>
                    </q-card>
                  </div></div>
                  <div class="col-2"><div class="q-pa-md">
                    <q-card flat>
                      <q-item>
                        <q-item-section avatar>
                          <q-avatar square icon="img:statics/equipment.svg" size="120px"></q-avatar>
                        </q-item-section>
                      </q-item>
                      <q-card-section style="text-align: left!important;margin-left: 25px;padding-right: -25px">
                        <div style="font-size: 22px">{{ $t('avtar1.tip') }}</div>
                        <br>
                        <div style="font-size: 14px">{{ $t('avtar1.tip_note') }}</div>
                      </q-card-section>
                    </q-card>
                  </div></div>
                  <div class="col-2"></div>
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
  background-position: right center;
  box-shadow: 0 12px 20px -11px #5b86e5;
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
