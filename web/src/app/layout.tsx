import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Public APIs - Free API Directory",
  description: "A curated collection of free public APIs for developers. Browse, search, and discover APIs for your next project.",
  keywords: ["API", "public APIs", "free APIs", "developer tools", "API directory"],
  openGraph: {
    title: "Public APIs - Free API Directory",
    description: "A curated collection of free public APIs for developers",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
