<template>
    <q-scroll-area :thumb-style="thumbStyle"
                 :bar-style="barStyle"
                 :visible="visible"
                 :delay="1500"
                 ref="scrollArea"
                 @scroll="onScroll()"
                 :style="{ height: scroll_height, width: width }"
  >
  <q-layout view="lHh Lpr lFf">
    <q-header style="background-color:#1370ee; display: flex;">
      <q-toolbar style="align-self:center;">
          <q-btn
            size="25px"
            icon="img:statics/logo.svg"
            unelevated:true
            flat
            to="/"
            style="margin: 0 10px 0 18.75%">
          </q-btn>
        <q-toolbar-title style="font-size: 20px;font-weight: bold;max-width: 8.85%" to="/">
          {{ $t('index.title') }}
        </q-toolbar-title>
        <q-space />
        <q-btn-group flat style="margin-left: 20.83%">
          <q-btn :label=navbar.front_page style="font-size: 16px;" to="/"></q-btn>
          <q-btn :label=navbar.community style="font-size: 16px;" to="/bbs"></q-btn>
          <q-btn :label=navbar.market style="font-size: 16px;"></q-btn>
          <q-btn-dropdown :label=navbar.demo>
            <q-list>
              <q-item clickable v-close-popup @click="ios">
                <q-item-section>
                  <q-item-label>IOS</q-item-label>
                </q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="android">
                <q-item-section>
                  <q-item-label>Android</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="ipad">
                <q-item-section>
                  <q-item-label>Ipad</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="windows">
                <q-item-section>
                  <q-item-label>Windows</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
          <q-btn
            :label=navbar.contact
            style="font-size: 16px;"
            @click="contact = true"
          ></q-btn>
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
      </q-toolbar>
    </q-header>
<!--    蓝色背景-->
    <svg width="100%" height="100%" viewBox="0 0 1920 880" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <g id="页面-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="首页" fill="#1370EE">
          <path d="M0,0 L1920,0 L1920,599.84668 C1920,651.063565 1881.30299,694.001406 1830.3618,699.308397 L110.3618,878.495887 C55.4306103,884.218551 6.26094715,844.32716 0.538283207,789.39597 C0.179669518,785.953679 -3.75978507e-14,782.495091 0,779.034171 L0,0 L0,0 Z" id="矩形"></path>
        </g>
      </g>
    </svg>
        <svg width="100%" height="100%" viewBox="0 0 1920 880" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <g id="页面-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="首页" fill="#1370EE">
          <path d="M0,0 L1920,0 L1920,599.84668 C1920,651.063565 1881.30299,694.001406 1830.3618,699.308397 L110.3618,878.495887 C55.4306103,884.218551 6.26094715,844.32716 0.538283207,789.39597 C0.179669518,785.953679 -3.75978507e-14,782.495091 0,779.034171 L0,0 L0,0 Z" id="矩形"></path>
        </g>
      </g>
    </svg>
<!--  联系我们-->
  <q-dialog v-model="contact">
      <q-card style="width: 680px;height: 498px">
        <q-bar style="height: 70px;background-color:white;">
            <span style="font-size: 24px;font-weight: bold;color: black;margin-left: 43%;                                                                                                                               ">{{ $t('index.navbar.contact') }}</span>
          <q-space/>
          <q-btn dense flat icon="close" v-close-popup>
          </q-btn>
        </q-bar>
        <hr/>
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
                <q-input
                  v-model="text"
                  filled
                  type="textarea"
                  style="width: 100%; height: 100%"
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
<script>
import { defineComponent } from 'vue'
import { LocalStorage } from 'quasar'
import { openURL } from 'quasar'
import { useMeta  } from 'quasar'

export default defineComponent({
  name: 'Index',
  data () {
    return {
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
      scroll_width: this.$q.screen.height + '' + 'px',
      scroll_height: this.$q.screen.height + '' + 'px',
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
    }
  },
  methods: {
    frontpage () {
      openURL('https://production.56yhz.com/#/')
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
      console.log(this.$refs.scrollArea.getScrollPercentage())
    },
    ios () {
     openURL('http://www.quasarchs.com/vue-components/button/')
    },
    android () {
      openURL('http://www.quasarchs.com/vue-components/button/')
    },
    ipad () {
      openURL('http://www.quasarchs.com/vue-components/button/')
    },
    windows () {
      openURL('http://www.quasarchs.com/vue-components/button/')
    }
  },
  created() {
    var _this = this
    console.log(_this.$q.screen)
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
  setup () {
    // needs to be called in setup()
    useMeta({
      title: 'GreaterWMS',
      titleTemplate: title => `${title} - Open Source Warehouse Management System`,
      meta: {
        description: { name: 'description', content: 'GreaterWMS - Open Source Warehouse Management System' },
        keywords: { name: 'keywords', content: 'Quasar website' },
        equiv: { 'http-equiv': 'Content-Type', content: 'text/html; charset=UTF-8' },
        // note: for Open Graph type metadata you will need to use SSR, to ensure page is rendered by the server
        ogTitle:  {
          property: 'og:title',
          // optional; similar to titleTemplate, but allows templating with other meta properties
          template (ogTitle) {
            return `${ogTitle} - GreaterWMS`
          }
        }
      },
    })
  },
  watch: {
    lang (lang) {
      var _this = this
      LocalStorage.set('lang', lang)
      _this.$i18n.locale = lang
    }
  }
})
</script>
