<template>
    <li class=" border border-sky-800 hover:border-green-600 h-auto  rounded-lg">

        <!-- job desc tag  -->
        <span class="flex justify-between items-center text-xs md:text-sm">
            <ul class="flex flex-col mt-2 gap-2 h-20">
                <li class=" p-1 px-2  bg-green-300 text-green-800 rounded-e-xl w-20" v-if="featured">Nổi bật</li>
                <li class="p-1 px-2  bg-orange-300 text-orange-700 rounded-e-xl w-20" v-if="urgent">Gấp</li>
            </ul>

            <ul>
                <li class="p-1 px-2  bg-red-300 text-red-800 rounded-xl mr-4 w-20 text-center">{{level}}
                </li>
            </ul>
        </span>

        <!-- job desc  -->
        <span class="flex flex-col items-center justify-center mx-4">
            <img :src="logo" alt="logo company"
                class="w-20 h-auto hover:cursor-pointer" />
            <div class="text-center mt-4">
                <h5 class=" text-sky-900 font-bold text-sm md:text-base lg:text-xl hover:cursor-pointer hover:text-green-700">{{job}}</h5>
                <p class="text-gray-500 text-xs md:text-sm lg:text-base">{{ desc }}</p>
            </div>
        </span>

        <!-- salary and number of position  -->
        <span class="flex justify-between items-center mx-2 md:mx-4 lg:mx-6 xl:mx-8 mt-10 mb-4">
            <div class="text-amber-700 font-bold text-sm md:text-base lg:text-lg xl:text-xl">
                {{ salary }}
            </div>

            <div class="bg-sky-900 p-2 rounded-2xl text-xs md:text-sm lg:text-base text-yellow-100">{{ position }} vị trí</div>
        </span>
    </li>
</template>

<script lang="ts">
export default {
    props: {
        featured: {
            type: Boolean,
            required: false,
        },
        urgent: {
            type: Boolean,
            required: false,
        },
        level: {
            type: String,
            required: true,
        },
        logo: {
            type: String,
            required: true,
        },
        job: {
            type: String,
            required: true,
        },
        desc: {
            type: String,
            required: true,
        },
        salary: {
            type: String,
            required: true,
        },
        position: {
            type: Number,
            required: true,
        },
    }
}
</script>