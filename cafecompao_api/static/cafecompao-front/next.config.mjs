/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ['localhost'],
  },
  webpack:{ 
    watch: false
	},
};

export default nextConfig;
