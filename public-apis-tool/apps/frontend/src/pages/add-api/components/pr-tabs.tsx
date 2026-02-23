import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import React from "react";
import PRForm from "./pr-form";
import PRHistory from "./pr-history";

const PRTabs = () => {
  return (
    <div className="w-full mb-12">
      <Tabs defaultValue="add" className="w-full">
        <div className="flex justify-center">
          <TabsList variant="line" className="w-fit">
            <TabsTrigger value="add" className="w-32">
              Add API
            </TabsTrigger>
            <TabsTrigger value="history" className="w-32">
              PR History
            </TabsTrigger>
          </TabsList>
        </div>

        <TabsContent value="add" className="mt-6 w-full">
          <PRForm />
        </TabsContent>
        <TabsContent value="history" className="mt-6 w-full">
          <PRHistory />
        </TabsContent>
      </Tabs>
    </div>
  );
};

export default PRTabs;
