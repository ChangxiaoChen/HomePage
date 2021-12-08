<template>
  <q-layout view="lHh Lpr lFf">
    <q-header style="background-color:#1370ee;height: 110px;display: flex;">
      <q-toolbar style="align-self:center;">
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            size="25px"
            icon="img:statics/logo.svg"
            unelevated:true
            flat
            @click="frontpage"
            style="margin: 0 10px 0 360px">
          </q-btn>
        </transition>
        <q-toolbar-title style="font-size: 20px;font-weight: bold;max-width: 150px">
          GreaterWMS
        </q-toolbar-title>
        <q-btn-group flat style="margin-left: 412px">
          <q-btn label="首页" style="font-size: 16px;"></q-btn>
          <q-btn label="社区" style="font-size: 16px;"></q-btn>
          <q-btn label="软件下载" style="font-size: 16px;"></q-btn>
          <q-btn label="产品介绍" style="font-size: 16px;"></q-btn>
          <q-btn
            label="联系我们"
            style="font-size: 16px;"
            @click="contact = true"
          ></q-btn>
<!--          选择语言下拉框-->
          <q-btn-dropdown label="English">
            <q-list>
              <q-item clickable v-close-popup @click="langChange(language.value)">
                <q-item-section>
                  <q-item-label>简体中文</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="langChange(language.value)">
                <q-item-section>
                  <q-item-label>日本</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup @click="langChange(language.value)">
                <q-item-section>
                  <q-item-label>繁体中文</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
        </q-btn-group>
      </q-toolbar>
    </q-header>
    <svg width="100%" height="100%" viewBox="0 0 1920 880" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <g id="页面-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="首页" fill="#1370EE">
          <path d="M0,0 L1920,0 L1920,599.84668 C1920,651.063565 1881.30299,694.001406 1830.3618,699.308397 L110.3618,878.495887 C55.4306103,884.218551 6.26094715,844.32716 0.538283207,789.39597 C0.179669518,785.953679 -3.75978507e-14,782.495091 0,779.034171 L0,0 L0,0 Z" id="矩形"></path>
        </g>
      </g>
    </svg>
  </q-layout>
  <q-dialog v-model="contact">
      <q-card style="width: 680px;height: 498px">
        <q-bar style="height: 80px;background-color:white;">
            <span style="font-size: 24px;color: black;margin-left: 43%">联系我们</span>
          <q-space/>
          <q-btn dense flat icon="close" v-close-popup>
          </q-btn>
        </q-bar>
        <hr/>
      </q-card>
  </q-dialog>
</template>
<router-view />
<script>
export default {
  data () {
    return {
      contact: false
    }
  },
  methods: {
    frontpage () {
      window.open('https://production.56yhz.com/#/')
    },
    langChange (e) {
      var _this = this
      _this.lang = e
      window.setTimeout(() => {
        location.reload()
      }, 1)
    }
  }
}
</script>
