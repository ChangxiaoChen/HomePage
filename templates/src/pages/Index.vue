<template>
  <q-page class="flex flex-center">
    {{baseurl}}
    <q-btn @click="getList()">111</q-btn>
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import { baseurl, get } from "boot/axios";

export default defineComponent({
  name: 'PageIndex',
  data () {
    return {
      baseurl: baseurl
    }
  },
  methods: {
    getList () {
      get('https://www.56yhz.com/area_v2/?auth=singosgu').then(res=>{
        console.log(res)
      }).catch(err=>{
        console.log(err)
      })
    }
  }
})
</script>
