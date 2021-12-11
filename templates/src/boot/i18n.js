import { boot } from 'quasar/wrappers'
import { createI18n } from 'vue-i18n'
import messages from 'src/i18n'
import { LocalStorage } from 'quasar'

var lang = LocalStorage.getItem('lang')
if (LocalStorage.has('lang')) {
  lang = lang || 'en-US'
} else {
  LocalStorage.set('lang', 'en-US')
  lang = 'en-US'
}

const i18n = new createI18n({
  locale: lang,
  fallbackLocale: lang,
  messages
})

export default ({ app }) => {
  app.use(i18n)
}

export { i18n }
