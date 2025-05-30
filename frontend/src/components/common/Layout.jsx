import Header from "@/components/common/Header";
import Footer from "@/components/common/Footer";

export default function Layout({ children }) {
    return (
        <div className="min-h-screen flex flex-col">
            <Header />

            <main className="flex-1 container mx-auto px-4 py-6">
                {children}
            </main>

            <Footer />
        </div>
    );
}
