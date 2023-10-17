<template>
    <main class="pt-16 lg:pt-20 bg-gray-200">
        <div class="px-20 flex flex-col lg:flex-row mt-20">
            <!-- search engine -->
            <div class=" basis-1/4 bg-white shadow-sm p-4 rounded-lg flex flex-col gap-6">
                <div class="flex justify-between">
                    <h1 class=" text-xs md:text-sm lg:text-lg font-bold text-sky-950">Tìm kiếm công việc</h1>
                    <button class="text-xs md:text-sm lg:text-base text-slate-600">Xóa</button>
                </div>
                <div class="flex flex-col gap-3">
                    <input type="text" placeholder="Vị trí tuyển dụng" class="border border-sky-900 px-4 py-3 rounded-md w-full outline-none focus:border-green-600">
                    <input type="text" placeholder="Địa điểm" class="border border-sky-900 px-4 py-3 rounded-md w-full outline-none focus:border-green-600">
                </div>

                <!-- Category  -->
                <div class="flex flex-col gap-4">
                    <span class="flex items-center justify-between">
                        <h1 class="text-xs md:text-sm lg:text-base font-semibold">Thể loại</h1>
                        <font-awesome-icon icon="fa-solid fa-chevron-up" class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer" v-if="!isExpandCategory" @click="expand('category')"/>
                        <font-awesome-icon icon="fa-solid fa-chevron-down" class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer" v-else @click="expand('category')"/>
                    </span>
                    <ul class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base" v-if="isExpandCategory">
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="frontend">
                            <label for="frontend">Frontend (31)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="backend">
                            <label for="backend">Backend (20)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="security">
                            <label for="security">Security (4)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="AI">
                            <label for="AI">AI (20)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="data">
                            <label for="data">Data Engineer (12)</label>
                        </li>
                    </ul>
                </div>

                <!-- Location  -->
                <div class="flex flex-col gap-4">
                    <span class="flex items-center justify-between">
                        <h1 class="text-xs md:text-sm lg:text-base font-semibold">Địa điểm làm việc</h1>
                        <font-awesome-icon icon="fa-solid fa-chevron-up" class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer" v-if="!isExpandLocation" @click="expand('location')"/>
                        <font-awesome-icon icon="fa-solid fa-chevron-down" class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer" v-else @click="expand('location')"/>
                    </span>
                    <ul class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base" v-if="isExpandLocation">
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="hanoi">
                            <label for="hanoi">Hà Nội (31)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="danang">
                            <label for="danang">Đà nẵng (20)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="hcm">
                            <label for="hcm">TP. Hồ Chí Minh (4)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="nhatrang">
                            <label for="nhatrang">Nha Trang (20)</label>
                        </li>
                    </ul>
                </div>

                <!-- Skills  -->
                <div class="flex flex-col gap-4">
                    <span class="flex items-center justify-between">
                        <h1 class="text-xs md:text-sm lg:text-base font-semibold">Kỹ năng</h1>
                        <font-awesome-icon icon="fa-solid fa-chevron-up" class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer" v-if="!isExpandSkills" @click="expand('skills')"/>
                        <font-awesome-icon icon="fa-solid fa-chevron-down" class="text-xs md:text-sm lg:text-base p-1 bg-green-300 rounded-full text-green-900 hover:cursor-pointer" v-else @click="expand('skills')"/>
                    </span>
                    <ul class="flex flex-col gap-2 text-slate-600 text-xs md:text-sm lg:text-base" v-if="isExpandSkills">
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="html">
                            <label for="html">HTML, CSS, Javascript (102)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="vue">
                            <label for="vue">VueJS (46)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="node">
                            <label for="node">NodeJS (4)</label>
                        </li>
                        <li class="flex gap-2 items-center">
                            <input type="checkbox" id="react">
                            <label for="react">ReactJS (20)</label>
                        </li>
                    </ul>
                </div>

                <!-- Salary  -->
            </div>
        </div>
    </main>
</template>

<script lang="ts">
    export default {
        data() {
            return {
                isExpandCategory: false,
                isExpandLocation: false,
                isExpandSkills: false
            }
        },
        methods: {
            expand(type: String) {
                switch(type) {
                    case 'category':
                        this.isExpandCategory = !this.isExpandCategory;
                        break;
                    case 'location':
                        this.isExpandLocation = !this.isExpandLocation;
                        break;
                    case 'skills':
                        this.isExpandSkills = !this.isExpandSkills;
                        break;
                }
            }
        }
    }
</script>