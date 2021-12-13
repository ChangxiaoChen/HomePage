<template>
    <q-scroll-area :thumb-style="thumbStyle"
                   :bar-style="barStyle"
                   :visible="visible"
                   :delay="1500"
                   ref="scrollAreaHome"
                   @scroll="onScroll()"
                   :style="{ height: scroll_height, width: scroll_width }"
  >
    <q-layout view="hhh LpR fFf" class="bg-grey-1">
      <q-header class="bg-grey-3 shadow-24" reveal>
        <q-toolbar class="GPLAY__toolbar text-black">
           <q-btn
             icon="img:statics/logo.svg"
             round
             dense
             unelevated
             flat
             to="/"
           />
           <q-toolbar-title>
            <a class="text-black" href="/" style="text-decoration:none">
              {{ $t('index.title') }}
            </a>
          </q-toolbar-title>
          <q-space />
          <div class="GPLAY__toolbar-input-container row no-wrap">
            <q-input dense outlined square placeholder="Search" class="bg-white col" />
            <q-btn class="" color="primary" icon="search" unelevated />
          </div>
          <q-space />
          <div class="q-pl-md q-gutter-sm row no-wrap items-center">
            <q-btn v-show="langlable !== '简体中文'" round flat icon="img:icons/Github.png" @click="goTo('https://github.com/Singosgu/GreaterWMS')" />
            <q-btn v-show="langlable === '简体中文'" round flat icon="img:icons/gitee.ico" @click="goTo('https://gitee.com/Singosgu/GreaterWMS')" />
            <q-btn-group>
              <q-btn v-show="langlable !== '简体中文'" color="primary" label="Login" />
              <q-btn v-show="langlable === '简体中文'" color="primary" label="登入" />
              <div style="border:1px solid; float:left;height:5px; color: #1976D2"></div>
              <div style="border:1px solid; float:left;height:5px; color: #1976D2; margin-top: 31px; margin-left: -2px"></div>
              <q-btn v-show="langlable !== '简体中文'" color="primary" label="Register" />
              <q-btn v-show="langlable === '简体中文'" color="primary" label="注册" />
            </q-btn-group>
            <q-btn v-show="langlable !== '简体中文'" round flat label="CN" @click="langChange('zh-hans')" />
            <q-btn v-show="langlable === '简体中文'" round flat label="EN" @click="langChange('en-US')" />
          </div>
        </q-toolbar>
      </q-header>
      <q-page-container>
        <q-page padding>
          <div class="q-pa-md">
              <div class="row">
                <div class="col-2">
                  这里不要写代码
                </div>
                <div class="col-2">
                  Manu固定写在这里
                </div>
                <div class="col-6">
                  新路由，写个子页面，作为这个页面的childrenp
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <p>新路由，写个子页面，作为这个页面的children</p>
                  <router-view />
                </div>
                <div class="col-2">
                  这里不要写代码
                </div>
              </div>
            </div>
           <q-page-sticky v-show='pagelocation > 0.5' position="bottom-right" :offset="[18, 18]" @click="ScrollToTop()">
            <q-fab
              icon="arrow_upward"
              color="primary"
            >
            </q-fab>
          </q-page-sticky>
        </q-page>
      </q-page-container>
    </q-layout>
    </q-scroll-area>
</template>

<style lang="sass">
.GPLAY
  &__toolbar-input-container
    min-width: 100px
    width: 25%
  &__toolbar-input-btn
    border-radius: 0
    max-width: 60px
    width: 100%
</style>
<script>
import { defineComponent, ref } from 'vue'
import { openURL, Screen, createMetaMixin, LocalStorage } from 'quasar'

export default defineComponent({
  name: 'Home',
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
      scroll_width: Screen.width + '' + 'px',
      scroll_height: Screen.height + '' + 'px',
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#027be3',
        width: '8px',
        opacity: 0.75
      },
      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#027be3',
        width: '12px',
        opacity: 0.2
      },
      pagelocation: 0
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
      _this.pagelocation = _this.$refs.scrollAreaHome.getScrollPercentage().top
      console.log(_this.$refs.scrollAreaHome.getScrollPercentage())
    }
  },
  created() {
    var _this = this
    _this.title = 'GreaterWMS - 开源社区'
    _this.meta = {
      description: {name: 'description', content: 'GreaterWMS - Open Source Warehouse Management System'},
      keywords: {name: 'keywords', content: 'Quasar website'},
      equiv: {'http-equiv': 'Content-Type', content: 'text/html; charset=UTF-8'},
      ogTitle: {
        property: 'og:title',
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
    const scrollAreaHome = ref(null)
    return {
      position,
      scrollAreaHome,
      ScrollToTop () {
        scrollAreaHome.value.setScrollPosition('vertical', position.value, 100)
      }
    }
  }
})
</script>
