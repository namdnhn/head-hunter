<template>
    <li class="bg-slate-50 border border-sky-800 hover:border-green-600 h-auto  rounded-lg">

        <!-- job desc  -->
        <span class="pt-20 flex flex-col items-center justify-center mx-4">
            <img :src="logo" alt="logo company"
                class="w-20 h-auto hover:cursor-pointer" />
            <div class="text-center mt-4">
                <router-link :to="companyDetailPage" class=" text-sky-900 font-bold text-sm md:text-base lg:text-xl hover:cursor-pointer hover:text-green-700">{{ companyName }}</router-link>
                <p class="text-gray-500 text-xs md:text-xs lg:text-base">{{ companyDescription }}</p>
                <span class="text-gray-500 text-xs md:text-sm lg:text-base">
                    <font-awesome-icon :icon="['fas', 'location-dot']" /> {{ companyAddress }}
                </span>
            </div>
        </span>

        <!-- salary and number of position  -->
        <span class="flex justify-between items-center mx-2 md:mx-4 lg:mx-6 xl:mx-8 mt-10 mb-4 gap-1">
            <div class="bg-sky-900 p-2 rounded-2xl text-xs md:text-xs lg:text-base text-yellow-100 hover:cursor-pointer hover:bg-sky-700">Đánh giá</div>

            <div class="bg-sky-900 p-2 rounded-2xl text-xs md:text-xs lg:text-base text-yellow-100 hover:cursor-pointer hover:bg-sky-700">Xem công ty</div>
        </span>
    </li>
</template>

<script lang="ts">
export default {
    props: {
        id: {
            type: String,
            required: true,
        },
        logo: {
            type: String,
            required: true,
        },
        companyName: {
            type: String,
            required: true,
        },
        companyDescription: {
            type: String,
            required: true,
        },
        companyAddress: {
            type:String,
            required: true,
        }
    },
    computed: {
        companyDetailPage() {
            return "/companyDetailPage" ;
        }
    }
}
</script>