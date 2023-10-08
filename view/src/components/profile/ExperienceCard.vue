<template>
    <li class="flex items-center gap-2 lg:gap-4">
        <img :src="logo" alt="company logo"
            class=" w-16 h-auto">
        <span class="flex flex-col">
            <h2 class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold">{{ name }}</h2>
            <ul class="flex mt-1 md:mt-0 flex-col md:flex-row lg:gap-4 text-xs lg:text-sm text-gray-500">
                <li>
                    <h3 class="text-sky-800 font-semibold">{{ role }}
                    </h3>
                </li>
                <li>
                    {{ time }}
                </li>
                <li>
                    {{ duration }}
                </li>
            </ul>
        </span>
    </li>
</template>

<script lang="ts">
    export default {
        props: {
            logo: {
                type: String,
                required: true,
            },
            name: {
                type: String,
                required: true,
            },
            role: {
                type: String,
                required: true,
            },
            time: {
                type: String,
                required: true,
            },
            duration: {
                type: String,
                required: true,
            },
        }
    }
</script>