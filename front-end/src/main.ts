import { createApp } from 'vue'
import './style.css'
import './index.css'
import App from './App.vue'
import router from './router.ts'

// import base component 
import BaseDialog from './components/ui/BaseDialog.vue'
import BaseList from './components/ui/BaseList.vue'
import JobCard from './components/ui/JobCard.vue'
import CategoryCard from './components/ui/CategoryCard.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo, faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass, faCode, faComputer, faRobot, faDatabase } from '@fortawesome/free-solid-svg-icons'


/* add icons to the library */
library.add(faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo,faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass, faCode, faComputer, faRobot, faDatabase)

const app = createApp(App)

app.use(router)

// add font icon 
app.component('font-awesome-icon', FontAwesomeIcon)

// add components 
app.component('BaseDialog', BaseDialog)
app.component('BaseList', BaseList)
app.component('JobCard', JobCard)
app.component('CategoryCard', CategoryCard)

app.mount('#app')
