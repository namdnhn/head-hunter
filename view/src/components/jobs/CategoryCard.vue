<template>
    <li class="flex flex-col p-10 bg-white justify-center items-center shadow-md rounded-lg">
        <font-awesome-icon :icon="icon" class=" text-3xl md:text-4xl lg:text-5xl text-green-600 mb-2" />
        <a href="#" class="hover:text-green-700 font-semibold text-sm md:text-base lg:text-lg text-sky-950 p-2">{{ job }}</a>
        <span class="bg-gray-100 p-2 rounded-xl text-xs md:text-sm lg:text-base">{{ quantity }} công việc</span>
    </li>
</template>

<script lang="ts">
    export default {
        props: {
            icon: {
                type: String,
                required: true
            },
            job: {
                type: String,
                required: true
            }, 
            quantity: {
                type: Number,
                required: true
            }
        }
    }
</script>