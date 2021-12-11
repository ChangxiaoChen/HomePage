<template>
    <q-scroll-area :thumb-style="thumbStyle"
                 :bar-style="barStyle"
                 :visible="visible"
                 :delay="1500"
                 ref="scrollArea"
                 @scroll="onScroll()"
                 :style="{ height: scroll_height, width: width }"
  >
  <q-layout view="hHh LpR fFf" class="bg-grey-3">
    <q-header class="bg-grey-3 shadow-24" reveal height-hint="60">
      <q-toolbar class="GPLAY__toolbar text-black">
         <q-btn
            icon="img:statics/logo.svg"
            unelevated:true
            flat
            to="/"
         />
         <q-toolbar-title style="font-size: 20px;font-weight: bold;max-width: 8.85%" to="/">
          {{ $t('index.title') }}
        </q-toolbar-title>
        <q-space />
        <div class="GPLAY__toolbar-input-container row no-wrap">
          <q-input dense outlined square placeholder="Search" class="bg-white col" />
          <q-btn class="" color="primary" icon="search" unelevated />
        </div>
        <q-space />
        <div class="q-pl-md q-gutter-sm row no-wrap items-center">
          <q-btn round flat icon="img:icons/Github.png" />
          <q-btn-group>
            <q-btn color="primary" label="登入" />
            <q-btn color="primary" label="注册" />
          </q-btn-group>
          <q-btn v-show="langlable !== '简体中文'" round flat label="EN" />
          <q-btn v-show="langlable === '简体中文'" round flat label="CN" />
        </div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
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
      console.log(_this.$refs.scrollArea.getScrollPercentage())
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
