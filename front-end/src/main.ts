import { createApp } from 'vue'
import './style.css'
import './index.css'
import App from './App.vue'
import router from './router.ts'

// import component 
import BaseDialog from './components/ui/BaseDialog.vue'
import BaseList from './components/ui/BaseList.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo, faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'


/* add icons to the library */
library.add(faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo,faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass)

const app = createApp(App)

app.use(router)

// add font icon 
app.component('font-awesome-icon', FontAwesomeIcon)

// add components 
app.component('BaseDialog', BaseDialog)
app.component('BaseList', BaseList)

app.mount('#app')
