import "./globals.css";
import Layout from "@/components/common/Layout";
import Providers from "@/components/Providers";

export const metadata = {
  title: "Mi Tienda",
  description: "E-commerce básico",
};

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body>
        <Providers>
          <Layout>{children}</Layout>
        </Providers>
      </body>
    </html>
  );
}
