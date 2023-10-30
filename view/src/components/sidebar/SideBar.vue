<template>
	<main class="fixed top-0 left-0 right-0 h-full z-40 bg-white">
		<nav class="fixed top-0 z-50 w-full bg-white border-b border-lime-600">
			<div class="px-3 py-3 lg:px-5 lg:pl-3 bg-white">
				<div class="flex items-center justify-between">
					<div class="flex items-center justify-start">
						<button
							data-drawer-target="logo-sidebar"
							data-drawer-toggle="logo-sidebar"
							aria-controls="logo-sidebar"
							type="button"
							class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
						>
							<span class="sr-only">Open sidebar</span>
							<svg
								class="w-6 h-6"
								aria-hidden="true"
								fill="currentColor"
								viewBox="0 0 20 20"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									clip-rule="evenodd"
									fill-rule="evenodd"
									d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
								></path>
							</svg>
						</button>
						<a
							href=""
							class="flex ml-2 md:mr-24 border-emerald-500"
						>
							<img
								src="../../assets/logo.png"
								class="h-8 mr-3"
								alt=""
							/>
							<span
								class="self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-black"
								>Head Hunter</span
							>
						</a>
					</div>
					<div
						class="flex items-center justify-center font-bold text-3xl text-indigo-900"
					>
						Sun* Inc Company
					</div>
					<div class="flex items-center justify-end">
						<div class="flex items-center ml-3">
							<div class="text-blue-500 font-semibold">
								<img
									class="h-16 w-16 rounded-full"
									src="https://scontent.fhan9-1.fna.fbcdn.net/v/t39.30808-6/358101051_1788127444936881_4807402604074812217_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_ohc=tSMvN9N8JlcAX_tbu5H&_nc_ht=scontent.fhan9-1.fna&oh=00_AfDAyJN0CJ2QhWmB5kjLKvFH0kosO15iFwgZgrP9YruU0A&oe=653C7E0A"
									alt=""
								/>
							</div>
						</div>
					</div>
				</div>
			</div>
		</nav>

		<aside
			id="logo-sidebar"
			class="fixed top-8 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full bg-white border-r border-lime-600 sm:translate-x-0"
			aria-label="Sidebar"
		>
			<div class="h-full px-3 pb-4 overflow-y-auto bg-white">
				<ul class="space-y-2 font-medium">
					<li>
						<a
							href="#"
							class="flex items-center p-2 rounded-lg dark:text-black hover:bg-green-300"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M6 6.878V6a2.25 2.25 0 012.25-2.25h7.5A2.25 2.25 0 0118 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 004.5 9v.878m13.5-3A2.25 2.25 0 0119.5 9v.878m0 0a2.246 2.246 0 00-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0121 12v6a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 18v-6c0-.98.626-1.813 1.5-2.122"
								/>
							</svg>

							<span
								class="ml-3 whitespace-nowrap font-semibold text-xl"
								>Bảng công việc</span
							>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="flex items-center p-2 text-gray-900 rounded-lg dark:text-black hover:bg-green-300"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
								/>
							</svg>

							<span class="flex-1 ml-3 whitespace-nowrap"
								>Ứng viên của tôi</span
							>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="flex items-center p-2 text-gray-900 rounded-lg dark:text-black hover:bg-green-300"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z"
								/>
							</svg>

							<span class="flex-1 ml-3 whitespace-nowrap"
								>Tin nhắn</span
							>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="flex items-center p-2 text-gray-900 rounded-lg dark:text-black hover:bg-green-300"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M20.25 14.15v4.25c0 1.094-.787 2.036-1.872 2.18-2.087.277-4.216.42-6.378.42s-4.291-.143-6.378-.42c-1.085-.144-1.872-1.086-1.872-2.18v-4.25m16.5 0a2.18 2.18 0 00.75-1.661V8.706c0-1.081-.768-2.015-1.837-2.175a48.114 48.114 0 00-3.413-.387m4.5 8.006c-.194.165-.42.295-.673.38A23.978 23.978 0 0112 15.75c-2.648 0-5.195-.429-7.577-1.22a2.016 2.016 0 01-.673-.38m0 0A2.18 2.18 0 013 12.489V8.706c0-1.081.768-2.015 1.837-2.175a48.111 48.111 0 013.413-.387m7.5 0V5.25A2.25 2.25 0 0013.5 3h-3a2.25 2.25 0 00-2.25 2.25v.894m7.5 0a48.667 48.667 0 00-7.5 0M12 12.75h.008v.008H12v-.008z"
								/>
							</svg>

							<span class="flex-1 ml-3 whitespace-nowrap"
								>Bài đăng công việc</span
							>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="flex items-center p-2 text-gray-900 rounded-lg dark:text-black hover:bg-green-300"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M16.5 3.75V16.5L12 14.25 7.5 16.5V3.75m9 0H18A2.25 2.25 0 0120.25 6v12A2.25 2.25 0 0118 20.25H6A2.25 2.25 0 013.75 18V6A2.25 2.25 0 016 3.75h1.5m9 0h-9"
								/>
							</svg>

							<span class="flex-1 ml-3 whitespace-nowrap"
								>Hồ sơ đã nhận</span
							>
						</a>
					</li>
					<li>
						<a
							href="#"
							class="flex items-center p-2 text-gray-900 rounded-lg dark:text-black hover:bg-green-300"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M15.75 15.75l-2.489-2.489m0 0a3.375 3.375 0 10-4.773-4.773 3.375 3.375 0 004.774 4.774zM21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>

							<span class="flex-1 ml-3 whitespace-nowrap"
								>Tìm kiếm ứng viên</span
							>
						</a>
					</li>
					<li class="pt-">
						<a
							href="#"
							class="flex items-center p-2 text-gray-900 rounded-lg dark:text-black hover:bg-green-300"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75"
								/>
							</svg>

							<span class="flex-1 ml-3 whitespace-nowrap"
								>Đăng xuất</span
							>
						</a>
					</li>
				</ul>
			</div>
		</aside>

		<!--  -->

		<!-- body -->
		<!-- <div class="p-4 sm:ml-64 pt-2">
   <div class="p-4 pt-12 mt-14">
      <div class="grid grid-cols-3 gap-4 mb-4">
         <div class="flex items-center justify-center h-24 rounded bg-indigo-200">
         </div>
         <div class="flex items-center justify-center h-24 rounded bg-indigo-200">
         </div>
         <div class="flex items-center justify-center h-24 rounded bg-indigo-200">
         </div>
      </div>
      <div class="flex items-center justify-center h-48 mb-4 rounded bg-indigo-200">
      </div>
      <div class="grid grid-cols-2 gap-4 mb-4">
         <div class="flex items-center justify-center rounded bg-violet-200">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded  h-28 bg-violet-200">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded h-28 bg-violet-200">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded h-28 bg-violet-200">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
      </div>
      <div class="flex items-center justify-center h-48 mb-4 rounded bg-indigo-200">
         <p class="text-2xl text-gray-400 dark:text-gray-500">
         </p>
      </div>
      <div class="grid grid-cols-2 gap-4">
         <div class="flex items-center justify-center rounded  h-28 bg-fuchsia-300">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-fuchsia-300">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-fuchsia-300">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-fuchsia-300">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
      </div>
   </div>
   </div> -->
	</main>
</template>

<!-- <script lang="ts">
    export default {

    }
</script> -->
