export default {
	async getJobs(_: any) {
		let apiUrl = "http://localhost:8000/api/job";

		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch jobs."
			);
			throw error;
		}

        console.log(responseData);
        
        
		return responseData;
	},
	async getJob(_: any, id: any) {
		let apiUrl = "http://localhost:8000/api/job/" + id;

		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch job."
			);
			throw error;
		}

		responseData.deadline = new Date(
			responseData.deadline
		).toLocaleDateString("en-CA"); // 'en-CA' format is yyyy-mm-dd

		return responseData;
	},
	async getFeaturedJobs() {
		let apiUrl = "http://localhost:8000/api/job";
		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch jobs."
			);
			throw error;
		}

        let featured_jobs = []

        for (let i = 0; i < responseData.length; i++) {
            if (responseData[i].featured) {
                featured_jobs.push(responseData[i])
            }
        }

		return featured_jobs;
	},
	async createJob(_: any, jobData: any) {
		let apiUrl = "http://localhost:8000/api/job/create";

        console.log(jobData);
        

		const response = await fetch(apiUrl, {
			method: "POST",
			body: JSON.stringify(jobData),
			headers: {
				"Content-Type": "application/json",
			},
		});

		console.log(response);

		const responseData = await response.json();

		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to create job."
			);
			throw error;
		}

		return responseData;
	},
};
