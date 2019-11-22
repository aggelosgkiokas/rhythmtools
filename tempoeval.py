import numpy
# outdata, targets are numpy vectos of shape (n,) where n the number of excerpts to be evaluated.
def evaluate_tempo(outdata, targets):
    data_n = outdata.shape[0]
    acc1 = 0
    acc2 = 0

    for c in range(data_n):
        o = numpy.float32(outdata[c])
        t = numpy.float32(targets[c])
        if numpy.abs(o-t)/t < 0.04:
            acc1 = acc1 + 1

        acc2val = numpy.min([numpy.abs(o-2.0*t)/(2.0*t),numpy.abs(o-t*0.5)/(0.5*t), numpy.abs(o-3.0*t)/(3.0*t),numpy.abs(o-t/3.0)/(t/3.0), numpy.abs(o-t)/t])
        if  acc2val < 0.04:
            acc2 = acc2+1

    acc1 = acc1 / data_n
    acc2 = acc2 / data_n
    return [acc1, acc2]
