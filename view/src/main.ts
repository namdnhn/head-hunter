import { createApp } from 'vue'
import './style.css'
import './index.css'
import App from './App.vue'
import router from './router.ts'
import store from './store/index.ts'

// import base component 
import BaseDialog from './components/ui/BaseDialog.vue'
import BaseList from './components/ui/BaseList.vue'
import JobCard from './components/jobs/JobCard.vue'
import CategoryCard from './components/jobs/CategoryCard.vue'
import ExperienceCard from './components/profile/ExperienceCard.vue'
import CvCard from './components/profile/CvCard.vue'
import BaseSpinner from './components/ui/BaseSpinner.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo, faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass, faCode, faComputer, faRobot, faDatabase, faUserTie, faLocationDot, faCakeCandles, faUpload, faEnvelope, faPhone, faGraduationCap, faLayerGroup, faUser, faWallet, faBriefcase, faFile, faPenToSquare, faXmark, faAnglesLeft, faAnglesRight, faHeart, faBuilding,  } from '@fortawesome/free-solid-svg-icons'
import { faFacebook } from '@fortawesome/free-brands-svg-icons'
import { faLinkedin } from '@fortawesome/free-brands-svg-icons/faLinkedin'
import { faGoogle } from '@fortawesome/free-brands-svg-icons/faGoogle'
import { faStar } from '@fortawesome/free-regular-svg-icons'
import { faCircle } from '@fortawesome/free-regular-svg-icons/faCircle'
import { faCircleDot } from '@fortawesome/free-regular-svg-icons/faCircleDot'


/* add icons to the library */
library.add(faUserSecret, faChevronDown, faBars, faChevronUp, faBell, faChevronRight, faCircleInfo,faArrowRight, faLock, faArrowRightFromBracket, faMagnifyingGlass, faCode, faComputer, faRobot, faDatabase, faUserTie, faLocationDot, faCakeCandles, faUpload, faEnvelope, faPhone, faGraduationCap, faLayerGroup, faUser, faWallet, faBriefcase, faFacebook, faLinkedin, faFile, faGoogle, faPenToSquare, faXmark, faStar, faCircle,faCircleDot, faAnglesLeft, faAnglesRight, faHeart, faBuilding )

const app = createApp(App)

app.use(router)
app.use(store)

// add font icon 
app.component('font-awesome-icon', FontAwesomeIcon)

// add components 
app.component('BaseDialog', BaseDialog)
app.component('BaseList', BaseList)
app.component('JobCard', JobCard)
app.component('CategoryCard', CategoryCard)
app.component('ExperienceCard', ExperienceCard)
app.component('CvCard', CvCard)
app.component('BaseSpinner', BaseSpinner)

app.mount('#app')
