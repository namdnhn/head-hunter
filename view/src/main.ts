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
import ExperienceCard from './components/ui/ExperienceCard.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo, faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass, faCode, faComputer, faRobot, faDatabase, faUserTie, faLocationDot, faCakeCandles, faUpload, faEnvelope, faPhone, faGraduationCap, faLayerGroup, faUser, faWallet, faBriefcase, } from '@fortawesome/free-solid-svg-icons'
import { faFacebook } from '@fortawesome/free-brands-svg-icons'
import { faLinkedin } from '@fortawesome/free-brands-svg-icons/faLinkedin'
import { faGoogle } from '@fortawesome/free-brands-svg-icons/faGoogle'


/* add icons to the library */
library.add(faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo,faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass, faCode, faComputer, faRobot, faDatabase, faUserTie, faLocationDot, faCakeCandles, faUpload, faEnvelope, faPhone, faGraduationCap, faLayerGroup, faUser, faWallet, faBriefcase, faFacebook, faLinkedin, faGoogle  )

const app = createApp(App)

app.use(router)

// add font icon 
app.component('font-awesome-icon', FontAwesomeIcon)

// add components 
app.component('BaseDialog', BaseDialog)
app.component('BaseList', BaseList)
app.component('JobCard', JobCard)
app.component('CategoryCard', CategoryCard)
app.component('ExperienceCard', ExperienceCard)

app.mount('#app')
