<template>
    <main class="pt-16 lg:pt-20">
        <!-- Introduce  -->
        <div
            class=" bg-gray-100 px-10 md:px-24 lg:px-40 xl:px-60 py-10 flex flex-col lg:flex-row gap-6 justify-between items-center">
            <div class="flex flex-col md:flex-row items-center gap-6">
                <img src="https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/team-1.jpg" alt="candidate avt"
                    class="w-32 md:w-40 lg:w-48 h-auto rounded-full">
                <div class="flex flex-col justify-between items-center md:items-start gap-2 text-center md:text-start">
                    <h4 class="text-base md:text-lg lg:text-xl font-semibold text-sky-950">Nguyễn Đức Thiện</h4>
                    <!-- info  -->
                    <ul class="flex gap-4 items-center text-center md:text-start">
                        <li class="text-gray-700 text-xs md:text-sm lg:text-base">
                            <font-awesome-icon icon="fa-solid fa-user-tie" class="mr-1" />
                            Software Developer
                        </li>
                        <li class="text-gray-700 text-xs md:text-sm lg:text-base">
                            <font-awesome-icon icon="fa-solid fa-location-dot" class="mr-1 " />
                            Hà Nội
                        </li>
                        <li class="text-gray-700 text-xs md:text-sm lg:text-base">
                            <font-awesome-icon icon="fa-solid fa-cake-candles" class="mr-1 " />11-01-2003
                        </li>
                    </ul>

                    <!-- skills  -->
                    <ul class="grid grid-cols-3 gap-4 mt-4 text-center">
                        <li class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg">Design
                        </li>
                        <li class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg">PHP</li>
                        <li class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg">NodeJS
                        </li>
                        <li class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg">WordPress
                        </li>
                        <li class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg">VueJS
                        </li>
                        <li class="text-gray-500 text-xs md:text-sm lg:text-base py-1 px-4 bg-gray-200 rounded-lg">Python
                        </li>
                    </ul>
                </div>
            </div>

            <span
                class="p-4 bg-sky-900 rounded-lg text-yellow-100 hover:cursor-pointer hover:opacity-95 text-xs md:text-sm lg:text-base">Upload
                CV <font-awesome-icon icon="fa-solid fa-upload" class="ml-2" />
            </span>
        </div>

        <!-- Detail info  -->
        <div class="px-10 md:px-24 lg:px-40 xl:px-60 py-10">
            <!-- User info  -->
            <div>
                <!-- introduce  -->
                <div class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10">
                    <h1 class="text-base md:text-lg lg:text-xl font-bold text-sky-900">About Candidate</h1>
                    <p class="text-xs md:text-sm lg:text-base text-gray-600">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                        aliquip ex ea commodo consequat.
                    </p>
                    <p class="text-xs md:text-sm lg:text-base text-gray-600">
                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
                        anim id est laborum.
                    </p>
                </div>

                <!-- all info  -->
                <div class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10">
                    <h1 class="text-base md:text-lg lg:text-xl font-bold text-sky-900">All Infomation</h1>
                    <ul class="grid grid-cols-1 gap-6 md:grid-cols-2">

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-envelope"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">themezhub@gmail.com
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Mail Address</p>
                            </span>
                        </li>

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-phone"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">855 606 8472
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Phone Number</p>
                            </span>
                        </li>

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-user"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">Male
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Gender</p>
                            </span>
                        </li>

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-cake-candles"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">07 Apr 1992
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Date Of Birth</p>
                            </span>
                        </li>

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-wallet"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">$750/month
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Offer Salary</p>
                            </span>
                        </li>

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-briefcase"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">1 Year
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Experience</p>
                            </span>
                        </li>

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-graduation-cap"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">Bachelor Degree
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Qualification</p>
                            </span>
                        </li>

                        <li class="flex gap-4 items-center">
                            <font-awesome-icon icon="fa-solid fa-layer-group"
                                class=" bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
                            <span>
                                <h5 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">Level
                                </h5>
                                <p class="text-xs lg:text-sm text-gray-500">Junior</p>
                            </span>
                        </li>

                    </ul>
                </div>

                <!-- Experience  -->
                <div class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10">
                    <h1 class="text-base md:text-lg lg:text-xl font-bold text-sky-900">All Experience</h1>

                    <ul class="flex flex-col gap-4">
                        <experience-card v-for="company in companies" :key="company.id" :logo="company.logo"
                            :name="company.name" :time="company.time" :duration="company.duration"
                            :role="company.role"></experience-card>
                    </ul>

                </div>

                <!-- Education  -->
                <div class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10">
                    <h1 class="text-base md:text-lg lg:text-xl font-bold text-sky-900">Education</h1>

                    <ul class="flex flex-col gap-4">
                        <experience-card v-for="education in educations" :key="education.id" :logo="education.logo"
                            :name="education.name" :time="education.time" :duration="education.duration"
                            :role="education.role"></experience-card>
                    </ul>
                </div>

                <!-- Candidate skill  -->
                <div class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10">
                    <h1 class="text-base md:text-lg lg:text-xl font-bold text-sky-900">Candidate Skill</h1>

                    <ul class="flex gap-4">
                        <li
                            class="py-2 px-4 text-center text-sky-900 bg-green-300 rounded-xl text-xs md:text-sm lg:text-base">
                            Java
                        </li>
                        <li
                            class="py-2 px-4 text-center text-sky-900 bg-green-300 rounded-xl text-xs md:text-sm lg:text-base">
                            Python
                        </li>
                        <li
                            class="py-2 px-4 text-center text-sky-900 bg-green-300 rounded-xl text-xs md:text-sm lg:text-base">
                            VueJS
                        </li>
                        <li
                            class="py-2 px-4 text-center text-sky-900 bg-green-300 rounded-xl text-xs md:text-sm lg:text-base">
                            NodeJS
                        </li>
                    </ul>
                </div>

                <!-- Language  -->
                <div class="p-4 border border-green-400 rounded-lg flex flex-col gap-4 mb-10">
                    <h1 class="text-base md:text-lg lg:text-xl font-bold text-sky-900">Language</h1>

                    <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-10 lg:gap-20">
                        <li class="flex gap-2 items-center">
                            <h1
                                class="py-1 md:py-2 lg:py-3 w-10 md:w-12 lg:w-14 rounded-full bg-green-300 font-bold text-center text-sm md:text-base lg:text-lg">
                                JP</h1>
                            <span>
                                <h2 class="text-xs md:text-sm lg:text-base font-semibold text-sky-900">Japanese</h2>
                                <p class="text-gray-500 text-xs lg:text-sm">Basic</p>
                            </span>
                        </li>

                        <li class="flex gap-2 items-center">
                            <h1
                                class="py-1 md:py-2 lg:py-3 w-10 md:w-12 lg:w-14 rounded-full bg-green-300 font-bold text-center text-sm md:text-base lg:text-lg">
                                EN</h1>
                            <span>
                                <h2 class="text-xs md:text-sm lg:text-base font-semibold text-sky-900">English</h2>
                                <p class="text-gray-500 text-xs lg:text-sm">Advance</p>
                            </span>
                        </li>

                        <li class="flex gap-2 items-center">
                            <h1
                                class="py-1 md:py-2 lg:py-3 w-10 md:w-12 lg:w-14 rounded-full bg-green-300 font-bold text-center text-sm md:text-base lg:text-lg">
                                CN</h1>
                            <span>
                                <h2 class="text-xs md:text-sm lg:text-base font-semibold text-sky-900">Chinese</h2>
                                <p class="text-gray-500 text-xs lg:text-sm">Medium</p>
                            </span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- suggest jobs  -->
            <div>

            </div>
        </div>
    </main>
</template>

<script lang="ts">

export default {
    data() {
        return {
            companies: [
                {
                    id: 1,
                    logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-3.png",
                    name: "Google Inc.",
                    role: "Sr. Team Leader",
                    time: "4 Years 7 Month",
                    duration: "Feb 2017 - Present",
                },
                {
                    id: 2,
                    logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png",
                    name: "Linked In",
                    role: "Sr. Product Designer",
                    time: "2 Years 3 Month",
                    duration: "Aug 2015 - Jan 2017"
                }
            ],
            educations: [
                {
                    id: 1,
                    logo: "https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-4.png",
                    name: "Vietnam National University, Hanoi",
                    role: "Bachelor of Computer Science",
                    time: "4 Years",
                    duration: "Sep 2021 - Sep 2025",
                }
            ],
        }
    }
}
</script>