#ifndef ASCIISCALARREPORTWRITER_H_
#define ASCIISCALARREPORTWRITER_H_

#include "stats/ReportWriterInterface.h"
#include "stats/ScalarEstimator.h"
#include <fstream>

class AsciiScalarReportWriter: public ReportWriterInterface<ScalarEstimator> {
public:
    AsciiScalarReportWriter(std::ofstream& file);
    virtual ~AsciiScalarReportWriter();

    virtual void startReport(const ScalarEstimator& est);
    virtual void reportStep(const ScalarEstimator& est);

private:
    std::ofstream &file;
};

#endif