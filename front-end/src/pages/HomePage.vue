<template>
    <main class="pt-20 h-screen w-full">
        <div
            class="h-auto w-full bg-yellow-100 px-20 py-10 flex justify-evenly items-center"
        >
            <section class="text-sky-900">
                <h5 class="text-amber-700 mb-10 font-bold">
                    Get Hot & Trending Jobs
                </h5>
                <h1 class="text-5xl mb-10 font-bold">
                    Find & Hire <br />
                    Top Experts on Head <br />
                    Hunter
                </h1>
                <p class="text-lg mb-10">
                    Getting a new job is never easy. Check what new jobs we have
                    <br />
                    in store for you on Head Hunter.
                </p>
                <span>
                    <ul class="flex gap-10 font-bold">
                        <li class="flex flex-col">
                            <h2 class="flex text-5xl gap-2">
                                <span class="text-sky-900">200</span>
                                <span class="text-amber-700">M</span>
                            </h2>
                            <p>Active jobs</p>
                        </li>
                        <li class="flex flex-col">
                            <h2 class="flex text-5xl gap-2">
                                <span class="text-sky-900">40</span>
                                <span class="text-amber-700">M</span>
                            </h2>
                            <p>Startups</p>
                        </li>
                        <li class="flex flex-col">
                            <h2 class="flex text-5xl gap-2">
                                <span class="text-sky-900">300</span>
                                <span class="text-amber-700">K</span>
                            </h2>
                            <p>Talents</p>
                        </li>
                    </ul>
                </span>
            </section>

            <!-- Search Jobs -->
            <form action="" class="h-auto p-10 bg-white rounded-lg">
                <h1 class="text-5xl text-sky-900 mb-8 font-bold">
                    Grow Your Career With <br />
                    <span class="text-amber-700">Head Hunter</span>
                </h1>

                <!-- Search jobs keyword  -->
                <div class="relative mb-8">
                    <div
                        class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                    >
                        <svg
                            class="w-4 h-4 text-gray-500 dark:text-gray-400"
                            aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 20 20"
                        >
                            <path
                                stroke="currentColor"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                            />
                        </svg>
                    </div>
                    <input
                        type="search"
                        class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Search Jobs Keywords"
                    />
                </div>

                <!-- job category and job type  -->
                <div class="flex gap-12 items-center justify-between mb-8">
                    <span class="flex flex-col w-full">
                        <label for="category" class="text-sm mb-2"
                            >Job Category</label
                        >
                        <select
                            name="category"
                            id="category"
                            class="p-2 border rounded-md min-w-full"
                        >
                            <option value="">Software & Application</option>
                            <option value="">Software & Application</option>
                            <option value="">Software & Application</option>
                            <option value="">Software & Application</option>
                        </select>
                    </span>

                    <span class="flex flex-col w-full">
                        <label for="type" class="text-sm mb-2">Job Type</label>
                        <select
                            name="type"
                            id="type"
                            class="p-2 border rounded-md min-w-full"
                        >
                            <option value="">All type</option>
                            <option value="">All type</option>
                            <option value="">All type</option>
                            <option value="">All type</option>
                        </select>
                    </span>
                </div>

                <!-- job level and experience  -->
                <div class="flex gap-12 items-center justify-between mb-8">
                    <span class="flex flex-col w-full">
                        <label for="level" class="text-sm mb-2"
                            >Job Level</label
                        >
                        <select
                            name="level"
                            id="level"
                            class="p-2 border rounded-md min-w-full"
                        >
                            <option value="">Fresher</option>
                            <option value="">Fresher</option>
                            <option value="">Fresher</option>
                            <option value="">Fresher</option>
                        </select>
                    </span>

                    <span class="flex flex-col w-full">
                        <label for="experience" class="text-sm mb-2"
                            >Job Experience</label
                        >
                        <select
                            name="experience"
                            id="experience"
                            class="p-2 border rounded-md min-w-full"
                        >
                            <option value="">1 year</option>
                            <option value="">1 year</option>
                            <option value="">1 year</option>
                            <option value="">1 year</option>
                        </select>
                    </span>
                </div>

                <!-- expected salary  -->
                <div class="flex flex-col w-full">
                    <label for="salary" class="text-sm mb-2"
                        >Expected Salary</label
                    >
                    <select
                        name="salary"
                        id="salary"
                        class="p-2 border rounded-md min-w-full"
                    >
                        <option value="">500$</option>
                        <option value="">500$</option>
                        <option value="">500$</option>
                        <option value="">500$</option>
                    </select>
                </div>

                <!-- submit button  -->
                <button
                    type="submit"
                    class="bg-sky-900 text-yellow-100 rounded-lg p-4 mt-10 w-full"
                >
                    Search Result
                </button>
            </form>
        </div>

        <!-- Featured Jobs -->
        <div class="px-20 py-10">
            <h2 class="text-center text-lg leading-8 font-semi-bold mb-10">
                Join over 2,000 companies around the world <br />
                that trust the
                <span class="text-amber-700 font-bold">Head Hunter</span>
                platforms
            </h2>
            <span class="text-center mb-10">
                <h1 class="text-3xl font-extrabold mb-2">Featured Jobs</h1>
                <p class=" text-gray-400">
                    At vero eos et accusamus et iusto odio dignissimos ducimus
                    qui blanditiis praesentium voluptatum <br> deleniti atque
                    corrupti quos dolores
                </p>
            </span>

            <!-- Featured Jobs list -->
            <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
                <li>
                    <div class=" border border-green-600 h-atuo">

                        <!-- job desc tag  -->
                        <span class="flex justify-between text-sm">
                            <ul class="flex flex-col">
                                <li class="border border-rose-400 p-1 rounded-md">Featured</li>
                                <li>Urgent</li>
                            </ul>

                            <ul>
                                <li>Intership</li>
                            </ul>
                        </span>

                        <span>
                            
                        </span>

                        <span>

                        </span>

                    </div>
                </li>
            </ul>

        </div>
    </main>
</template>
