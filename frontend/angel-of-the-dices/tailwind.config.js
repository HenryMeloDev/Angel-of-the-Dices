/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
          sans: ["DM Sans", "sans-serif"],
      },
      fontWeight: {
          regular: 400,
          medium: 500,
          bold: 700,
        },
        fontSize: {
          xs: "0.875rem", // 12px
          xs: "0.875rem", // 14px
          sm: "1rem", // 16px
          base: "1.125rem", // 18px
          lg: "1.5rem", // 24px
          lg2: "2rem", // 32px
          xl: "2.5rem", // 40px
          "2xl": "3rem", // 48px
          "3xl": "3.25rem", // 52px
          "4xl": "3.375rem", // 54px
        },
        colors: {
          bgPrimary: "#1e1e1e",
          primary: "#39316e",
          secondary: "#483A9E",
          third: "#6B57EB",
          foth: "#352B75",
          fifth: "#231C4D",
          darkgrayColor: "#242124",
          lightgrayColor: "#8C92AC",
          bgSecondary: "#0D0C1D",
        },
      },
  },
  plugins: [],
}
