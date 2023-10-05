<template>
    <header
        class="h-12 md:h-16 lg:h-20 w-full fixed bg-white flex justify-center shadow-md"
    >
        <div class="w-11/12 flex justify-between">
            <nav class="flex items-center">
                <!-- Menu icon  -->
                <span
                    @click="toggleShowMenu"
                    class="md:hidden w-6 h-6 mr-4 hover:cursor-pointer hover:text-green-600"
                >
                    <font-awesome-icon
                        icon="fa-solid fa-bars"
                        class="w-6 h-6"
                    />
                </span>

                <!-- Logo -->
                <a class="mr-16 hover:cursor-pointer">
                    <img
                        src="https://scontent.fhan19-1.fna.fbcdn.net/v/t1.15752-9/384534050_247749267831715_7212647508339862763_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=R5Z7_XnavcAAX-FQAcZ&_nc_ht=scontent.fhan19-1.fna&oh=03_AdTfictJZUik_UDPUrJkBQjuB903QG1ileKFgJNew0kdZw&oe=6545E272"
                        alt="logo"
                        class="w-10 h-10 md:w-12 md:h-12 lg:w-14 lg:h-14"
                    />
                </a>

                <!-- Menu bars on small screen -->
                <ul
                    v-show="showMenu"
                    class="md:hidden flex flex-col gap-4 absolute top-12 left-0 w-full bg-gray-100"
                >
                    <li
                        class="mx-2 mt-2 p-4 bg-white flex items-center justify-between"
                    >
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Trang chủ</a
                        >
                    </li>
                    <li
                        class="mx-2 p-4 bg-white flex items-center justify-between"
                        @click="toggleMoreInfo('jobs')"
                    >
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Việc làm
                        </a>
                        <font-awesome-icon icon="fa-solid fa-chevron-down" v-if="!moreInfoJobs"/>
                        <font-awesome-icon icon="fa-solid fa-chevron-up" v-else/>
                    </li>
                    <li
                        class="mx-2 p-4 bg-white flex items-center justify-between"
                        @click="toggleMoreInfo('companies')"
                    >
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Công ty
                        </a>
                        <font-awesome-icon icon="fa-solid fa-chevron-down" v-if="!moreInfoCompanies"/>
                        <font-awesome-icon icon="fa-solid fa-chevron-up" v-else/>
                    </li>
                    <li
                        class="mx-2 mb-2 p-4 bg-white flex items-center justify-between"
                        @click="toggleMoreInfo('profiles')"
                    >
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Hồ sơ
                        </a>
                        <font-awesome-icon icon="fa-solid fa-chevron-down" v-if="!moreInfoProfiles"/>
                        <font-awesome-icon icon="fa-solid fa-chevron-up" v-else/>
                    </li>
                </ul>

                <!-- Menu on large screen -->
                <ul class="hidden md:flex gap-6">
                    <li>
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Trang chủ</a
                        >
                    </li>
                    <li>
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Việc làm
                            <font-awesome-icon icon="fa-solid fa-chevron-down"
                        /></a>
                    </li>
                    <li>
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Công ty
                            <font-awesome-icon icon="fa-solid fa-chevron-down"
                        /></a>
                    </li>
                    <li>
                        <a
                            class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                            >Hồ sơ
                        </a>
                    </li>
                </ul>
            </nav>

            <!-- login, logout  -->
            <span class="flex gap-4 items-center">
                <a
                    class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                    >Đăng nhập</a
                >
                <a
                    class="hover:text-green-700 hover:cursor-pointer text-xs md:text-sm lg:text-base"
                    >Đăng ký</a
                >
            </span>
        </div>
    </header>
</template>

<script lang="ts">
export default {
    data() {
        return {
            showMenu: false,
            moreInfoJobs: false,
            moreInfoCompanies: false,
            moreInfoProfiles: false,
        };
    },
    methods: {
        toggleShowMenu() {
            this.showMenu = !this.showMenu;
        },
        toggleMoreInfo(type: string) {
            switch (type) {
                case "jobs":
                    this.moreInfoJobs = !this.moreInfoJobs;
                    break;
                case "companies":
                    this.moreInfoCompanies = !this.moreInfoCompanies;
                    break;
                case "profiles":
                    this.moreInfoProfiles = !this.moreInfoProfiles;
                    break;
            }
        },
    },
};
</script>
